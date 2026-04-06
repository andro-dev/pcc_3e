from string import ascii_letters
from random import choice


def generate_sequence(items_to_generate: int, numbers: int = [], letters: str = []):
    """Generate random sequence of numbers and letters returning winning combination for a lottery ticket.
    Number of "tokens" in the sequence controlled by parameter: "how_many_to_generate"
    """

    if not numbers:
        numbers = list(range(1, 10))

    if not letters:
        letters = list(ascii_letters)

    combined_list = []
    result_list = []

    if numbers and letters and (len(numbers) + len(letters) >= items_to_generate):
        combined_list = numbers + letters
    else:
        print("Incorrect number of numbers and/or letters")
        return

    while len(result_list) < items_to_generate:
        pulled_item = str(choice(combined_list))
        if pulled_item not in result_list:
            result_list.append(
                str(choice(combined_list))
            )  # numbers converted to their character representations
        else:
            continue

    return result_list  # list of letters including character represented numbers. e.g.: ['a', 'Z', '2', '9']


def compare_two_sequences(seq1, seq2, disregard_position=True, disregard_case=True):
    # return True - if seq1 and seq2 have same contents
    # return False - otherwise
    # TODO: implement disregard_position = False and disregard_case=False cases

    result = False
    if len(seq1) == len(seq2) and sorted("".join(seq1).upper()) == sorted(
        "".join(seq2).upper()
    ):
        result = True
    return result
