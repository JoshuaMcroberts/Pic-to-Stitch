filename = "tm"
file = open("C:/Users/Joshu/Desktop/" + filename + ".jef", "wb")

int = [124, 0, 0, 0, 20, 0, 0]

for i in int:
    file.write(bytes((i,)))

file.close()