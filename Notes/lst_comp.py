names = ['Kieran', 'Suki', 'Alex', 'Serada', 'Jeff', 'Fin', 'Alfonzo']

people = [('Kieran', 'Prasch', 'Instructor'), ('Alfonzo', 'Ward', 'Student'), ('Fin', 'Balnik', 'Student')]


# long names - Return a list of names that are least `n` chars in length.
# starts_with - Return a list of names that start with `'S'`.
# last_names - Return a list of only last names from the list of tuples.
# smoosh - collapse the list of tuples `people` into a flat list of strings.

def long_names(n, names):
    new_list = [i for i in names if len(i) >= n]
    print(new_list)

def starts_with(names):
    new_list = [i for i in names if i[0] == 'S']
    print(new_list)

def last_names(people):
    new_list = [i[1] for i in people]
    print(new_list)

def smoosh(people):
    new_list = [x for i in people for x in i]
    print(new_list)

smoosh(people)