#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(min(list_length, len(my_list_1), len(my_list_2))):
        try:
            if isinstance(my_list_1[i], int) and isinstance(my_list_2[i], int):
                result = my_list_1[i] / my_list_2[i]
                new_list.append(result)
            else:
                new_list.append(0)
                print("wrong type")
        except ZeroDivisionError:
            new_list.append(0)
            print("division by 0")
        finally:
            pass
    if i < list_length - 1:
        print("out of range")
    return new_list
