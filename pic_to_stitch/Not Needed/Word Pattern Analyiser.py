

filename = "Common Word in Order"
file = open("C:/Users/Joshu/Desktop/"+ filename + ".txt", "r")

content = file.read()

content_list = content.split()
new_content_list = []
for x in content_list:
    print(x)
    word = list(x)
    values = []
    letters = []
    pattern = []
    letter_count = 0
    print("Word: ", word)
    for letter in word:
        print("Letters: ", letters)
        if letter in letters:
            index = letters.index(letter)
            pattern.append(values[index])
        else:
            letters.append(letter)
            letter_count += 1
            values.append(str(letter_count))
            pattern.append(str(letter_count))
    sep = ""


    # ** Used for finding only pattern words
    # length = len(pattern)
    # i = 1
    # null_word = str()
    # while i < length+1:
    #     null_word = null_word + str(i)
    #     i += 1

    pattern_word = sep.join(pattern)

    # print(pattern_word, type(pattern_word), null_word, type(null_word))
    # if pattern_word != null_word:
    new_string = x + " " + pattern_word
    new_content_list.append(new_string)

new_file = open("C:/Users/Joshu/Desktop/" + filename + " Patterns.txt", "w+")

for x in new_content_list:
    new_file.write(x + "\n")

new_file.close()
