sloka = open('aigiri_test2.txt', 'r')
sloka_txt = sloka.read()
sloka.close()

words = sloka_txt.split()
uni_file = open('unicode_test2.txt', 'w')

for i in words:
    if(i !='|' and i !='||' and not(i.isdigit())):
        for j in i:
            uni_file.write('U+' + hex(ord(j)).replace('x', ''))
            uni_file.write('  ')

uni_file.close()