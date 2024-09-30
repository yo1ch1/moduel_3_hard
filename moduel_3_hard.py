data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calc(data):
    result = 0
    if isinstance(data, (int, float)):
        result += data
    elif isinstance(data, str):
        result += len(data)
    elif isinstance(data, (list, tuple, set)):
        for elem in data:
            result += calc(elem)
    elif isinstance(data, dict):
        for key, value in data.items():
            result += calc(key)
            result += calc(value)

    return result
print(calc(data_structure))

