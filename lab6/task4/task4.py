import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(fn) -> list[dict]:
    with open(fn, 'r') as f:
        headers = f.readline()
        print("headers is",headers)
        headers = headers.split(",")
        header = [p.rstrip() for p in headers]
        list_d = []
        for lst in f:
            lst = lst.split(',')
            lst = [x.rstrip() for x in lst]
            lst = dict(zip(header, lst))
            list_d.append(lst)
    return list_d

# TODO реализовать конвертер из csv в json

#...You ever have that feeling where you're not sure if you're awake or still dreaming ?

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
