import re

from exceptions import KeyValueError, IndexValueError


def search(data_array, query):
    if isinstance(data_array, list):
        return search_list(data_array, query)
    elif isinstance(data_array, dict):
        return search_dict(data_array, query)
    else:
        raise TypeError("Unsupported data type")


def search_list(data_list, query):
    findings = []
    for i, item in enumerate(data_list):
        if isinstance(item, (list, dict)):
            sublist_findings = search(item, query)
            if sublist_findings:
                findings.append({f"index[{i}]": sublist_findings})
        elif isinstance(query, str) and query.lower() in item.lower() or \
                isinstance(query, int) and query == item:
            findings.append({f"index[{i}]": item})
    return findings


def search_dict(data_dict, query):
    findings = []
    for key, value in data_dict.items():
        if isinstance(value, (list, dict)):
            sublist_findings = search(value, query)
            if sublist_findings:
                findings.append({key: sublist_findings})
        elif (isinstance(query, str) and query.lower() in value.lower() or
              isinstance(key, str) and query.lower() in key.lower()) or \
                (isinstance(query, int) and query == value or isinstance(key, int) and query == key):
            findings.append({key: value})
    return findings


def _locator(data_dict, locator: str) -> int | str | list | dict | bool | float:
    dict_locator = {
        # 'content': ""
    }
    exec(f"dict_locator['content'] = data_dict{locator}")
    return dict_locator['content']


def add_data(data_dict: dict, content_locator: str = None, new_index: int = None, new_key: str = None,
             new_value: int | str | list | dict | bool | float = None, to_list=False):
    """
    The function allows adding values, index or keys to a JSON file.
    :param data_dict:
    :param content_locator: str -> The path to the item you want to add to. -> [0]['Name]...
            If the content locator is None, then the item is added to the file without hierarchy
    :param new_index: int -> the place where you want to input the variable.
            If the item is a list, it must include an index
    :param new_key: str -> the key that you want to add or an existing key that you want to add a value to.
            If the item is a dictionary, it must include a key
    :param new_value: The value that you want to add.
    :param to_list: True, if you want to add the value to a list, otherwise False -
            False is the default. -> only if type - only if the type is str, int, or float.
    """
    # check if content_locator is None - if True insert to content the whole content
    if content_locator is None:
        content = data_dict
    else:
        content = _locator(data_dict, content_locator)

    # content = file_content[content_locator]
    tyc = type(content)
    if tyc == dict:
        if new_key is None:
            raise KeyError("For dictionary type must insert a key")
        content = _add_data_dict(content, new_key, new_value)
    elif tyc == list:
        content = _add_data_list(content, new_index, new_value)
    elif tyc == str:
        content = _add_data_str(content, new_value, to_list)
    elif tyc == float or tyc == int:
        content = _add_data_num(content, new_value, to_list)
    elif tyc == bool:
        content = _add_data_bool(content, new_value)
    elif content is None:
        content = new_value
        # self._add_data_none(content, new_value)

    exec(f"data_dict{content_locator} = content")


def remove_data(data_dict: dict, content_locator: str, key: str | int = None, index: int = None):
    """
    removes specific data from json for type -> list, dict only
    :param content_locator: str -> The path to the item you want to delete. -> [0]['Name]...
    Can't be None
    :param key: If the item is a dictionary, it must include a key
    :param index: If the item is a list, it must include an index
    """
    pattern = f"{key}']$" + f'|{key}"]$'
    if key is not None:
        if not re.findall(pattern, content_locator):
            raise KeyValueError('The key does not match the path content_locator')
    elif index is not None:
        if not re.findall(f"{index}]$", content_locator):
            raise IndexValueError('The index does not match the path content_locator')
    elif key is None and index is None:
        raise ValueError("Must enter a key if it's a dictionary or enter an index if it's a list.")

    exec(f"del data_dict{content_locator}")


def _add_data_dict(content: dict, key: str, new_value: int | str | list | dict | bool | float) -> dict:
    if key not in content:
        content[key] = new_value

    # if the key already exist
    elif key in content:
        if type(content[key]) is list:
            content[key].append(new_value)
        else:
            content[key] = [content[key], new_value]
    return content


def _add_data_list(content: list, index: int, new_value: int | str | list | dict | bool | float) -> list:
    content.insert(index, new_value)
    return content


def _add_data_str(content: str, new_value: int | str | list | dict | bool | float, to_list: bool) -> str | list:
    if type(new_value) is str and not to_list:
        content = content + " " + f"{new_value}"
    else:
        content = [content, new_value]
    return content


def _add_data_num(content: int | float, new_value: int | str | list | dict | bool | float,
                  to_list: bool) -> int | float | list:

    if type(new_value) in [int, float] and not to_list:
        content += new_value
    else:
        content = [content, new_value]
    return content


def _add_data_bool(content: bool, new_value: int | str | list | dict | bool | float) -> list:
    content = [content, new_value]
    return content






