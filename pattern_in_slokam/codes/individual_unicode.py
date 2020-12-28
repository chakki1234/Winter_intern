def read(file_name):
  sloka = open(file_name, 'r')
  sloka_txt = sloka.read()
  sloka.close()
  return sloka_txt

def split_to_words(txt, out_file_name):
  words = txt.split()
  uni_file = open(out_file_name, 'w')

  for i in words:
      if(i !='|' and i !='||' and not(i.isdigit())):
          for j in i:
              uni_file.write('U+' + hex(ord(j)).replace('x', ''))
              uni_file.write('  ')

  uni_file.close()

split_to_words(read('aigiri_test1.txt'), 'unicode_test1.txt')
split_to_words(read('aigiri_test2.txt'), 'unicode_test2.txt')
split_to_words(read('aigiri.txt'), 'unicode.txt')