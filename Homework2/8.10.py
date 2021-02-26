word = input()
wordnospaces = word.replace(" ", "")
newword = wordnospaces
newword = newword[::-1]

if newword == wordnospaces:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")