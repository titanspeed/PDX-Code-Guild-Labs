def longest_word(file):
    with open(file, 'r') as look:
        list1 = look.read().split()
        longest = {}
        for x in list1:
            if x in longest.keys():
                longest[x] += 1
            else:
                longest[x] = 1
        print(longest)
            # longest[x] = {x: (len(x))}
        longest_w = ''
        for c in longest.keys():
            if len(c) > len(longest_w):
                longest_w = c
        print(longest_w)


file1 = 'bacon.txt'
longest_word(file1)