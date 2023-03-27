# def search(data_array, query):
#     findings = []
#     for item in data_array:
#         matches = {}
#         for key, value in item.items():
#             if isinstance(value, list):
#                 found = [(i, v) for i, v in enumerate(value) if query.lower() in v.lower()]
#                 if found:
#                     matches[key] = found
#             elif isinstance(value, str) and query.lower() in value.lower():
#                 matches[key] = value
#         if matches:
#             findings.append([{k: v} for k, v in matches.items()])
#     return findings

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
                findings.append([{i: sublist_findings}])
        elif isinstance(item, str) and query.lower() in item.lower():
            findings.append(item)
    return findings

def search_dict(data_dict, query):
    findings = []
    for key, value in data_dict.items():
        if isinstance(value, (list, dict)):
            sublist_findings = search(value, query)
            if sublist_findings:
                findings.append({key: sublist_findings})
        elif isinstance(value, str) and query.lower() in value.lower():
            findings.append({key: value})
    return findings

