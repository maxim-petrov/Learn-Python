from random import choice

lottery = ['9', '5', '3', '1', '7', 'A', '4', 'P', '5', 'M', '8', 'R',
           '4']
my_ticket = ['5', '7', 'P', '4']


x = 1
while True:
    winning_ticket = [choice(lottery), choice(lottery),
                      choice(lottery), choice(lottery)]
    if winning_ticket != my_ticket:
        x += 1
    else:
        print(x)
        break

