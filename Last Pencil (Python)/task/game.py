from random import choice



moves = [1, 2, 3]
winner = ''
turns = 0
player2 = ''
pencils_left = ''
reduced_pencils = ''
print("How many pencils would you like to use: ")
while True:
    try:
        num_of_pencils = int(input())

    except ValueError:
        print("The number of pencils should be numeric")

    else:
        if num_of_pencils == 0:
            print("The number of pencils should be positive")
            continue
        pencils_left = num_of_pencils
        break


print("Who will be the first (John, Jack): ")
while True:
    player1 = input()
    if player1 == "John" or player1 == "Jack":
        break
    else:
        print("Choose between 'John' and 'Jack'")

bot = "Jack"
if player1 == "John":
    player2 = bot
elif player1 == "Jack":
    player2 = "John"


while pencils_left > 0:
    print("|" * pencils_left)
    if turns % 2 == 0:
        player = player1
    else:
        player = player2
    print(f"{player}'s turn!")
    if player == "John":
        while True:
            reduced_pencils = input()
            if not reduced_pencils.isnumeric() or int(reduced_pencils) < 1 or int(reduced_pencils) > 3:
                print("Possible values: '1', '2' or '3'")
                continue
            elif int(reduced_pencils) > pencils_left:
                print("Too many pencils were taken")
                continue
            break
    elif player == bot:
        for i in moves:
            if (pencils_left - i) % 4 == 1:
                reduced_pencils = i
        if pencils_left == 1:
            reduced_pencils = 1
        elif pencils_left % 4 == 1:
            reduced_pencils = choice(moves)

        print(reduced_pencils)

    pencils_left -= int(reduced_pencils)
    turns += 1
    if pencils_left == 0:
        if turns % 2 == 0:
            winner = player1
        else:
            winner = player2
        print(f"{winner} won!")
        break
