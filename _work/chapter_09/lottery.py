import helper_functions


class Lottery:
    def __init__(self, num_of_letters: int = 5, num_of_numbers: int = 10):
        self.number_of_numbers = num_of_numbers
        self.number_of_letters = num_of_letters

    def generate_winning_ticket(self):
        # Generate sequence(list) of letters and numbers - all represented as characters
        return helper_functions.generate_sequence(
            items_to_generate=4
        )  # two optional arguments: numbers[] and letters[] are omitted

    def verify_ticket(self, ticket, winning_ticket):
        if helper_functions.compare_two_sequences(seq1=ticket, seq2=winning_ticket):
            # print("Congratulations on winning the lottery!")
            # print(
            #     f"Your ticket: {ticket} matches the winning combination: {winning_ticket}\n"
            # )
            return True
        else:
            return False
