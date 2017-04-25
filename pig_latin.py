def pig_latin():
    vowels = ['A', 'E', 'I', 'O', 'U']
    consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    input1 = input('Please type a word to translate into pig latin: ').capitalize()
    p_word = list(input1)
    if p_word[0] in consonants:
        new_p = (input1[1:] + input1[:1].lower() + 'ay')
        print(new_p.capitalize())
    else:
        print(input1 + 'yay')

pig_latin()


