import csv
repetitions = {}
filename = input()


with open(filename, 'r') as csvfile:
    grades_reader = csv.reader(csvfile, delimiter=',')

    row_num = 1
    for row in grades_reader:
        for column in row:
            if repetitions.__contains__(column):
                repetitions[column] += 1
            else:
                repetitions[column] = 1


for rep in repetitions:
    print(rep, repetitions[rep])