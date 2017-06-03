dictionary = {}

def quantify_words(input):
    user_input = input(' ').split()
    for occurence in user_input:
        dictionary[occurence] = user_input.count(occurence)

quantify_words(input)
print(dictionary)
