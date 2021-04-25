# Brett Meirhofer 2036955

# Global variable
num_calls = 0


# TODO: Write the partitioning algorithm - pick the middle element as the
#       pivot, compare the values using two index variables l and h (low and high), 
#       initialized to the left and right sides of the current elements being sorted,
#       and determine if a swap is necessary
def partition(user_ids, i, k):
    midpoint = i  +  (k - i) // 2
    pivot = user_ids[midpoint]

    done = False
    x = i
    y = k

    while not done:
        while user_ids[x] < pivot:
            x = x + 1

        while pivot < user_ids[y]:
            y = y - 1

        if x >= y:
            done = True
        else:
            user_ids[x],user_ids[y] = user_ids[y],user_ids[x]
            x = x + 1
            y = y - 1




    return y


# TODO: Write the quicksort algorithm that recursively sorts the low and
#       high partitions. Add 1 to num_calls each time quisksort() is called
def quicksort(user_ids, i, k):
    global num_calls
    num_calls += 1
    if i >= k:
        return

    pi = partition(user_ids, i, k)
    quicksort(user_ids, i, pi)
    quicksort(user_ids, pi+1, k)


    return

if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    # Initial call to quicksort 
    quicksort(user_ids, 0, len(user_ids) - 1)

    # Print number of calls to quicksort
    print(num_calls)

    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)