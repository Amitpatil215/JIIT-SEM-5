file = open("test.txt", "r")

for line in file:

    line = line.strip("\n")
    words = line.split();

    for m in reversed(words):

    print('\n');

file.close()
