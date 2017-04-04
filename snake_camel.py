# def camel_to_snake(CamelString):

def snake_to_camel(snake_string):
    snake_list = snake_string.split("_")
    snake_list2 = []
    for snake in snake_list:
        snake_list2.append(snake.capitalize())
    print(snake_list2)
    return "".join(snake_list2)

snake_string = input('Place snake string here: ')

print (snake_to_camel(snake_string))
