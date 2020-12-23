#to read the unicode file
uni_file = open('unicode.txt', 'r')
uni_txt = uni_file.read()
uni_file.close()

#to write the characters in a new file
char_file = open('char.txt', 'a')

#converting unicode to characters
words = uni_txt.split()

for i in words:
    characters = i.split('U+')
    for j in characters:
        if(j != ''):
            j = j[:1] + 'x' + j[1:]
            char_file.write(chr(int(j, 16)))
    char_file.write(' ')

char_file.close()

    