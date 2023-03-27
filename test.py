from main import search
import json


if __name__ == '__main__':

    with open("example.json", "r") as fh:
        my_array = json.load(fh)
    print(search(my_array, "New"))

    # # desired outcome:
    # result = [
    #     [{'State': 'New York'},
    #     {'Cities': [(0, 'New York'), (2, 'New Platz')]},
    #     {'Rivers': [(2, 'Newtown Creek')]}],
    #     # [{'State': 'Illinois'},
    #      {'Cities': 'New Lenox'}]
    # ]


    my_list = ["1", "2", "3", "4", "5"]
    print(search(my_list, "4"))

    my_l = [1, 2, 3, [1, 2, 3], 5]
    print(search(my_l, 2))

    my_dict = {1:"old", 2:"new", 3:"borrowed", 4:"blue"}
    print(search(my_dict, 3))