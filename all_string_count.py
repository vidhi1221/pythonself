sentence = input("Enter Sentence : ")
total_count = {}
special_char = "~!@$%^&*"
upper = lower = digit = space = special = length = 0
for char in sentence:
    if char.isupper():
        upper += 1
        total_count["Uppercase"] = upper
    elif char.islower():
        lower += 1
        total_count["Lowercase"] = lower
    elif char.isdigit():
        digit += 1
        total_count["Digit"] = digit
    elif char.isspace():
        space += 1
        total_count["Space"] = space
    total_count["Length"] = len(sentence)

print(total_count)