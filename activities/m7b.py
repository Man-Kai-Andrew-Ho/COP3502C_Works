def parse_student(id_name_bday):
    dict_student = {"id": 0, "name": "", "birthdate": ""}
    new_list = list(id_name_bday)
    my_list = []
    for i in range(0,8):
        my_list.append(id_name_bday[i])
    dict_student["id"] = int("".join(my_list))

    index = 0
    for char in id_name_bday:
        if char.isdigit():
            continue
        else:
            dict_student["name"] += char
            index = id_name_bday.rfind(char)

    new_index = 0
    for num in range(index + 1, len(new_list)):
        new_index += 1
        if new_index == 2:
            dict_student["birthdate"] += str(id_name_bday[num]) + "/"
        else:
            dict_student["birthdate"] += str(id_name_bday[num])

    return dict_student

def count_items(my_list):
    dict_items = {}
    for i in range(len(my_list)):
        if my_list[i] in dict_items:
            continue
        else:
            dict_items[my_list[i]] = 1
        for j in range(i + 1, len(my_list)):
            if my_list[i] == my_list[j]:
                dict_items[my_list[i]] += 1

    return dict_items

def list_fighters(data):
    my_list = []
    my_list_second = []
    for key in data.keys():
        my_list_second.append(key)
        for keys in data[key].keys():
            my_list.append(data[key][keys])

    my_list.sort()
    my_list = sum(my_list, [])
    new_list = my_list + my_list_second
    new_list = list(sorted(set(new_list)))

    return new_list



