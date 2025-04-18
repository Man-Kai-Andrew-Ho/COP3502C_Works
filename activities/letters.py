word = input("Enter a word: ")
letter = input("Enter the letter to count: ")
counter = 0

for i in word:
    if i == letter:
        counter += 1

print(f"{letter} appears {counter} times.")