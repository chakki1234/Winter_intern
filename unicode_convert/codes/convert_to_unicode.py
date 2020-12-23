# to read the sloka file
sloka = open('aigiri.txt', 'r')
sloka_txt = sloka.read()
sloka.close()

#to convert the sloka to unicode 
words = sloka_txt.split()
uni_file = open('unicode.txt', 'w')

for i in words:
    if(i !='|' and not(i.isdigit())):
        for j in i:
            uni_file.write('U+' + hex(ord(j)).replace('x', ''))
        uni_file.write('  ')

uni_file.close()
    

