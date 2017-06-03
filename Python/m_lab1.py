import operator

def list_doubles(inp_list, n):
    return list(map(lambda x: x * n if x * n != 0, inp_list))

def list_doub(inp_list, n):
    return [operator.mul(x, n) for x in inp_list if x != 0]


list1 = [2, 2, 0]
print(list_doubles(list1, 2))
print(list_doub(list1, 2))