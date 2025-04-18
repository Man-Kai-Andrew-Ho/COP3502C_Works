def bin(n):
    num = n
    remain = ""
    if num == 0:
        return '0'
    else:
        while num >= 2:
            remain = remain + str(num % 2)
            num = num // 2
        if num == 1:
            remain = remain + "1"
    output = remain[::-1]
    return output

print(bin(10))

def capitalize(sentence):
    sentence = sentence.split(" ")
    new_list = []
    for word in sentence:
        word = word.capitalize()
        if word[0] == "O" or word[0] == "U" or word[0] == "S" or word[0] == "N" or word[0] == "D":
            word = word.lower()
        new_list.append(word)
    return " ".join(new_list)

def partition(numbers, n):
    result = []

    for i in range(0, len(numbers), n):
        sublist = numbers[i:i + n]
        result.append(sublist)
    return result
