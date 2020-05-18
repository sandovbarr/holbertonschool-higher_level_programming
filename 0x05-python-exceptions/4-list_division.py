#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newlist = []
    for n in range(list_length):
        try:
            division = my_list_1[n] / my_list_2[n]
        except TypeError:
            print('wrong type')
            division = 0
        except ZeroDivisionError:
            print('division by 0')
            division = 0
        except IndexError:
            print('out of range')
            division = 0
        finally:
            newlist.append(division)
    return newlist
