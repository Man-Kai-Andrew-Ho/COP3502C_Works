


def print_backwards(word):
    if len(word) == 1:
        print(word, end="")
        return
    else:
        print(word[-1], end="")
        return print_backwards(word[0:-1])

#try
# def format_names(names):
#     total = []
#     for name in names:
#         if "," in name:
#             total.append(name)
#         else:
#             new_name = name.split(" ")
#             new_name = new_name[::-1]
#             new_name = ", ".join(new_name)
#             total.append(new_name)
#     return total

def format_names(names):
    if not names:
        return []
    name = names[0]
    if "," in name:
        formatted_name = name
    else:
        parts = name.split(" ")
        formatted_name = ", ".join(parts[::-1])
    return [formatted_name] + format_names(names[1:])

def sum_a(dicts):
    if not dicts:
        return 0
    total = 0
    new_dict = dicts[0]
    if "a" in new_dict:
        total += new_dict["a"]
    return total + sum_a(dicts[1:])

def process_list(lists):
    total = []
    if lists[0] % 2 == 0:
        for num in lists:
            if num % 2 == 0:
                total.append(str(num))
        for nums in lists:
            if nums % 2 == 1:
                total.append(nums * 10)
    else:
        for num in lists:
            if num % 2 == 1:
                total.append(str(num))
        for nums in lists:
            if nums % 2 == 0:
                total.append(nums * 10)
    return total

