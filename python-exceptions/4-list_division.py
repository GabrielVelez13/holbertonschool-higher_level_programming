#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newList = []
    for item in range(list_length):
        try:
            div = my_list_1[item] / my_list_2[item]
        except ZeroDivisionError:
            div = 0
            print("division by 0")
        except TypeError:
            div = 0
            print("wrong type")
        except IndexError:
            div = 0
            print("out of range")
        finally:
            new_list.append(div)
    return newList
