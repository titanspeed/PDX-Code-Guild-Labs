class Book:
    def __init__(self, contents):
        self.contents = contents

    def count_words(self):
        count = 0
        with open(self.contents, 'r') as f:
            text = f.read().split()
            for x in text:
                count += 1
        print(count)

    def count_chars(self):
        count = 0
        with open(self.contents, 'r') as f:
            text = f.read()
            for x in text:
                count += 1
        print(count)

    def count_common(self):
        


