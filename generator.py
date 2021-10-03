"""
The program generator. You will find here everything that you need to complete
yourself for set up the program.
"""


# modes are the name of the different modes you want to be existing
modes = (
    "Classic",                 # mode 0
    "with special characters"  # mode 1
)


def generate(key: str, mode=0) -> str:
    """
    Generate a password according to the given key, for the specified mode

    :param key: The key used to generate the password
    :param mode: The generation mode
    :return: the generated password
    """

    if mode == 0:
        return "1965" + key             # generator for mode 0

    elif mode == 1:
        return "1965" + key + "@"       # generator for mode 1
