def count_lines(file):
    with open(file) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

file1 = 'bacon.txt'
print(count_lines(file1))

