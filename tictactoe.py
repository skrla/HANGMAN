def start_game():
    global field
    count = 0
    print("---------")
    print(f"""| {field[0]} {field[1]} {field[2]} |
| {field[3]} {field[4]} {field[5]} |
| {field[6]} {field[7]} {field[8]} |""")
    print("---------")
    while True:    #It's taking input and transforms the cordinates in index
        x, y = input("Enter the coordinates:").split()
        if x.isdigit() and y.isdigit():
            x = int(x) - 1
            y = int(y) + 2
            ind = (x * 3 + y) -3
            if x > 2 or y > 5:
                print("Coordinates should be from 1 to 3!")
                continue
            elif field[ind] != " ":
                print("This cell is occupied! Choose another one!")
                continue
        else:
            print("You should enter numbers!")
            continue
        count += 1
        if count % 2 == 0:    #Deciding if it's a X or O
            field[ind] = "O"
        else:
            field[ind] = "X"
        print("---------")
        print(f"""| {field[0]} {field[1]} {field[2]} |
| {field[3]} {field[4]} {field[5]} |
| {field[6]} {field[7]} {field[8]} |""")
        print("---------")
        if count > 4:    #Looks if there is a winner or if the game is a draw
                winingside = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
                for x in winingside:
                    if field[x[0]] == field[x[1]] == field[x[2]] == "X":
                        print("X wins")
                        return
                    elif field[x[0]] == field[x[1]] == field[x[2]] == "O":
                        print("O wins")
                        return
                if field.count("X") + field.count("O") == 9:
                    print("Draw")
                    return

field = [str(x).replace(str(x), " ") for x in range(10)]
start_game()
