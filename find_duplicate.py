def find_duplicate():
    x = input("Enter a word =")
    for char in x:
        counts = x.count(char)
        print(char, counts)

find_duplicate()