# string = input('Place CamelString here: ')
# string_list = []
# last_index = 0
#
# for i in range(len(string)):
#     if string[i].isupper():
#         if i != 0:
#             string_list.append(string[last_index:i])
#             last_index = i
#
# print(string_list)
# print('_'.join(string_list).lower())

# def camel_to_snake(CamelString):
#     camel_list = CamelString.split("A")
#     print(CamelString)
string = input('Place CamelString here: ')
string_list = []
last_index = 0
for i in range(len(string)):
    if string[i].isupper():
        if i != 0:
            string_list.append(string[last_index:i])
            last_index = i
            string_list.append(string[last_index:])

print('_'.join(string_list).lower())
