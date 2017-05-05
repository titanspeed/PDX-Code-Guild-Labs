units = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}
tens = {
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixy',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety'
}
teens = {
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen'
}
first_names = {'2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty', '6': 'sixty', '7': 'seventy', '8': 'eighty', '9': 'ninety'}
second_names = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '10': 'ten'}

def say_int(intg):
    norm = str(intg)
    if intg in units:
        print(units[intg])
    elif intg in teens:
        print(teens[intg])
    elif intg in tens:
        print(tens[intg])
    else:
        print(first_names[norm[0]] + ' ' + second_names[norm[1]])



user_choice = int(input('What Number?: '))
say_int(user_choice)