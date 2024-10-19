import sys
from collections import Counter

"""
Log analysis script

This script loads logs from a specified file and provides statistics on logging levels, 
as well as detailed information about logs of a specific level. It also handles errors such as
missing files and incorrect log formats.

Usage:
    python main.py path/to/logfile.log [LEVEL]

Arguments:
    path/to/logfile.log: the path to the log file to analyze.
    LEVEL: (optional) the logging level for which to display detailed information 
           (e.g., INFO, ERROR, DEBUG, etc.).

Output:
    - overall statistics by logging level with the count of entries for each level;
    - if a logging level is specified, detailed entries for that level are displayed;

Error Handling:
    - the script will print an error message and exit if the specified log file is not found;
    - if a log line format is incorrect, the script will report the error but continue processing;

Functions:
    load_logs(file_path: str) -> list:
        - loads logs from the specified file and returns them as a list of dictionaries;
        - handles errors for missing files and unexpected read errors;

    parse_log_line(line: str) -> dict:
        - parses a log line and returns a dictionary containing the date, time, level, and message;
        - reports errors for incorrect log line formats;

    filter_logs_by_level(logs: list, level: str) -> list:
        - filters the logs by the specified level and returns a list of entries for that level;

    count_logs_by_level(logs: list) -> dict:
        - counts the number of entries for each logging level and returns a dictionary with the results;

    display_log_counts(counts: dict):
        - displays the logging level statistics in a readable format;

    display_log_details(logs: list, level: str):
        - displays detailed information about logs for the specified level;

Example:
    python main.py logs.txt
    python main.py logs.txt error
"""



def load_logs(file_path: str) -> list:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            return list(map(parse_log_line, lines))
        
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: An unexpected error occurred while loading the file: {e}")
        sys.exit(1)
    
def parse_log_line(line: str) -> dict:
    try:
        log = {}
        date, time, level, *message = line.split()
        log["date"] = date
        log["time"] = time
        log["level"] = level
        log["message"] = " ".join(message)
        return log
    
    except ValueError:
        print("Error: The log line format is incorrect.")
        return None

def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log["level"] == level, logs))

def count_logs_by_level(logs: list) -> dict:
    levels = [log["level"] for log in logs]
    return dict(Counter(levels))

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("---------------- | -----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")

def display_log_details(logs: list, level: str):
    print(f"\nДеталі логів для рівня '{level}'")
    for log in logs:
        if log:
            print(f"{log['date']} {log['time']} - {log['message']}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        logs = load_logs(file_path)
        counts = count_logs_by_level(logs)  
        display_log_counts(counts)

        if len(sys.argv) > 2:
            level = sys.argv[2].upper()
            filtered_logs = filter_logs_by_level(logs, level)
            display_log_details(filtered_logs, level)

    
    

          
