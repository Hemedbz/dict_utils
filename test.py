from pprint import pprint

from main import *
import json


if __name__ == '__main__':

    with open("example.json", "r") as fh:
        my_array = json.load(fh)
    # pprint(search(my_array, "New"))

    m = {"State": "New York", "cities": ["New York", "Albeny", "New Paltz"]}
    with open("example2.json", "r") as f:
        # json.dump(m, f)
        my_array2 = json.load(f)

    # # desired outcome:
    # result = [
    #     [{'State': 'New York'},
    #     {'Cities': [(0, 'New York'), (2, 'New Platz')]},
    #     {'Rivers': [(2, 'Newtown Creek')]}],
    #     # [{'State': 'Illinois'},
    #      {'Cities': 'New Lenox'}]
    # ]


    # my_list = ["1", "2", "3", "4", "5"]
    # print(search(my_list, "4"))
    #
    # my_l = [1, 2, 3, [1, 2, 3], 5]
    # print(search(my_l, 2))
    # #
    # my_dict = {1:"old", 2:"new", 3:"borrowed", 4:"blue"}
    # print(search(my_dict, 3))
    #
    # print(search(my_array2, "new"))

    print(my_array2)
    add_data(my_array2, "['cities'][0]", new_value='www', to_list=False)
    print(my_array2)

    add_data(my_array2, "['State']", new_value='Abc', to_list=True)
    print(my_array2)

    add_data(my_array2, "['cities']", new_value='Abc', to_list=True, new_index=1)
    print(my_array2)

    remove_data(my_array2, "['cities'][1]", index=1)
    print(my_array2)

    remove_data(my_array2, "['cities']", key='cities')
    print(my_array2)

    val = ['aaa', 'bbb', {'abc':123, 'bla':456}]

    add_data(my_array2, new_value=val, new_key='cities')
    print(my_array2)