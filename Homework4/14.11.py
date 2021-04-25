# Brett Meirhofer 2036955

def selection_sort_descend_trace(numbers):
    for i in range(len(numbers)):
        MinIndex = i
        for j in range(len(numbers)):
            if(j >= i):
                if numbers[MinIndex] < numbers[j]:
                    MinIndex = j

        numbers[i], numbers[MinIndex] = numbers[MinIndex], numbers[i]
        if(i<len(numbers)-1):
            for x in numbers:
                print(str(x), end=" ")
            print()



if __name__ == "__main__":
    numbers = input().split(" ")
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    selection_sort_descend_trace(numbers)
    numbers = []
