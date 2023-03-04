"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the
Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

EXPECTED_BAKE_TIME = 40

PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes)
    derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int):
    """
    Calculate the preparation time.

    :param number_of_layers: int - the number of layers.
    :return: int - preparation tie (in minutes)
    derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the number of layers you want to add to the lasagna as
    an argument and returns how many minutes you would spend making them.
    Assume each layer takes 2 minutes to prepare.
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Calculate the preparation time.

    :param number_of_layers: int - the number of layers.
    :param number_of_layers: int - the number of minutes the lasagna has been
    baking in the oven.
    :return: int - time the lasagna has already spent baking in the oven
    (in minutes)

    return the total number of minutes you've been cooking, or the sum of your
    preparation time and the time the lasagna has already
    spent baking in the oven
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
