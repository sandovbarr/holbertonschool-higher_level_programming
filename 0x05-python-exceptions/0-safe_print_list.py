#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        counter = 0
        for counter in range(x):
            print("{}".format(my_list[counter]), end="")
            counter += 1
        print("") 
    except:
        print ("")
    finally:
        return (counter)
