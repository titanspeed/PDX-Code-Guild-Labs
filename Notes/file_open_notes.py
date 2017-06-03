def open_file():
    with open("bacon.txt", "r") as f:
        for i in f:
            f.readlines(-1)
            print(i)
    f.close()
open_file()