#Brett Meirhofer 2036955


if __name__ == '__main__':
    UserInput = input()
    Numbers = UserInput.split(" ")
    PositiveNumbers = []
    for Number in Numbers:
        Int = int(Number)
        if Int >= 0:
            PositiveNumbers.append(Int)

    PositiveNumbers.sort()
    for Number in PositiveNumbers:
        print(Number, end=" ")