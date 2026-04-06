from lottery import Lottery
from random import choice

lottery = Lottery()
winning_ticket = lottery.generate_winning_ticket()
# print(winning_ticket)
print("Winning Combination:", ", ".join(winning_ticket))

# 9-15 Lottery Analysis
''' 
    find how many randomly generated tickets required before the winning_ticket is generated+
'''
# Generate winning ticket: use winning_ticket already generated above
# Loop with counter starting at 1
counter = 1
while True:
#   Generate a lottery_ticket
    ticket = lottery.generate_winning_ticket()
#   If lottery_ticket has the same numbers/letters as winning_ticket
    if lottery.verify_ticket(ticket, winning_ticket):        
#       Print msg. - "Congratulations on winning a lottery. It took {counter} tickets to win the lottery"
        print("Congratulations on winning the lottery!")
        print(f"Your ticket: {ticket} matches the winning combination: {winning_ticket}")
        print(f"It took {counter:,} tickets to win")
        break
#   Else: increment the counter and continue loop
    else:
        counter += 1

