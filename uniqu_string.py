sentence = input("Enter Sentence : ")
words = sentence.split()
for word in words:
    if words.count(word) == 1:
        print(word)