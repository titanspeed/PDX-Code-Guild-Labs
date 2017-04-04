def reverse(string1):
    return string1[::-1]

def palindrome_check(string1, rstring):
    if string1 == rstring:
        return('Wow, that is a palindrome!')
    return 'NOPE, not a palindrome'

string1 = input('palindrome check: ')
rstring = reverse(string1)

print(palindrome_check(string1, rstring))

print(string1, rstring)
