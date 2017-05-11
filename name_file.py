def read_file(file, n):
    with open(file, 'r') as r:
        for line in file:
            print(r.readlines()[:n])


bacon = 'bacon.txt'
read_file(bacon, 2)
