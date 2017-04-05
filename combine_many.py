# Return the sum of any number of integers using *args.
# >>> combine_many(980, 667, 4432, 788, 122, 9, 545, 222)
# 7765

def combine_many(*args):
    return sum(integers for integers in args)

print(combine_many(1,982,345,1234))
