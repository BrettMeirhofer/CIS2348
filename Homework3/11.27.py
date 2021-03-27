#Brett Meirhofer 2036955


def OutputRoster(Roster):
    print("ROSTER")
    SortedKeys = sorted(Roster.keys())
    for X in SortedKeys:
        print("Jersey number: {}, Rating: {}".format(X,Roster[X]))
    print("")

def PrintMenu():
    print("MENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")
    print("")
    while True:
        print("Choose an option:")
        UserInput = input()

        if UserInput == "a":
            X = int(input("Enter a new player's jersey number:\n"))
            Y = int(input("Enter the player's rating:\n"))
            Players[X] = Y
            print("")
            PrintMenu()
            break

        if UserInput == "d":
            X = int(input("Enter a jersey number:\n"))
            Players.pop(X)
            print("")
            PrintMenu()
            break

        if UserInput == "u":
            X = int(input("Enter a jersey number:\n"))
            Y = int(input("Enter a new rating for player:\n"))
            Players[X] = Y
            print("")
            PrintMenu()
            break

        if UserInput == "r":
            TargetRating = int(input("Enter a rating:\n"))
            print("ABOVE", TargetRating)
            HighPlayers = {}
            for X,Y in Players.items():
                if Y > TargetRating:
                    HighPlayers[X] = Y

            SortedHighPlayers = sorted(HighPlayers.keys())
            for X in SortedHighPlayers:
                print("Jersey number: {}, Rating: {}".format(X, HighPlayers[X]))

            print("")



            PrintMenu()
            break

        if UserInput == "o":
            OutputRoster(Players)
            PrintMenu()
            break



        if UserInput == "q":
            break


Players = {}
for X in range(1,6):
    Number = int(input("Enter player {}'s jersey number:\n".format(X)))
    Rating = int(input("Enter player {}'s rating:\n".format(X)))
    Players[Number] = Rating
    print("")


OutputRoster(Players)

PrintMenu()