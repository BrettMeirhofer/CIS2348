#Brett Meirhofer 2036955

UserInput = input()
Words = UserInput.split()
Dict = {}
for word in Words:
    if word in Dict:
        Dict[word] += 1
    else:
        Dict[word] = 1

for word in Words:
    print(word, Dict[word])