import re


def generator_numbers(text: str):

    """
    Function to analyze text and identify all floating-point numbers that represent parts of income.

    Arguments:
    text (str): the string containing text in which to find floating-point numbers.

    Returns:
    generator: a generator that iterates over all floating-point numbers in the text.

    Uses a regular expression to find all floating-point numbers in the format X.XX, 
    where X is a digit. Floating-point numbers in the text must be clearly separated 
    by spaces on both sides and should be recorded without errors.
    """

    pattern = re.compile(r"\d+\.\d*")
    
    for match in re.finditer(pattern, text):
        yield match.group()


def sum_profit(text, generator_numbers):

    """
    Function to calculate the total profit based on floating-point numbers 
    obtained from the generator_numbers function.

    Arguments:
    text (str): the string containing text in which to find floating-point numbers.
    generator_numbers (Callable): the generator function that returns 
    floating-point numbers from the text.

    Returns:
    float: the total sum of floating-point numbers representing profit.
    """

    total = 0
    for i in generator_numbers(text):
        total += float(i)
    
    return total


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
