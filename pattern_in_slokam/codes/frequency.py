import matplotlib.pyplot as plt
import numpy as np

periodicity_found = []
periodicity = {}
processed_periodic_dict = {}
test_results = []

def read_and_split(file_name):
  sloka = open(file_name, 'r')
  sloka_txt = sloka.read()
  sloka.close()
  return sloka_txt.split()

def to_cal_periodicity(char, index, file_no):
    count = 0
    temp = uni_chars_list[file_no][index+1:]
    for j in temp:
        if j == char:
            periodicity[char].append(count)
            count = 0
        else:
            count = count + 1

def to_process_dict(periodicity_dict):
    dict_keys = periodicity_dict.keys()
    
    for key in dict_keys:
        if len(periodicity_dict[key]) == 0:
            average = 0
        else:
            average = sum(periodicity_dict[key])/len(periodicity_dict[key])
        key = key.replace('U+', '')
        key = key[:1] + 'x' + key[1:]
        processed_periodic_dict[chr(int(key, 16))] = average/len(aigiri_chars)

def plot_bar(periodicity_dict):
  values = list(periodicity_dict.values())
  keys = [ hex(ord(i)).replace('x', '') for i in list(periodicity_dict.keys()) ]

  fig = plt.figure()
  ax = fig.add_axes([0, 0, 5, 5])
  ax.bar(keys, values)
  plt.show()

uni_chars_list = []
aigiri_chars = read_and_split('unicode.txt')
uni_chars_list.append(read_and_split('unicode_test1.txt'))
uni_chars_list.append(read_and_split('unicode_test2.txt'))

for file_no, uni_chars in enumerate(uni_chars_list):
  global periodicity_found 
  global periodicity 
  global processed_periodic_dict 
  global test_results

  if file_no != 0:
    periodicity_found = []
    periodicity = {}
    processed_periodic_dict = {}

  for i, char in enumerate(uni_chars):
    if char in periodicity_found:
      pass
    else:
      periodicity_found.append(char)
      periodicity[char] = []
      to_cal_periodicity(char, i, file_no)
    
  print(periodicity)
  to_process_dict(periodicity)
  print(processed_periodic_dict)
  plot_bar(processed_periodic_dict)
  test_results.append(processed_periodic_dict)

common_keys = []
test1_result, test2_result = test_results

for i in  list(test1_result.keys()):
  if i in list(test2_result.keys()):
    common_keys.append(i)

key_value_1 = {}
key_value_2 = {}

for i in common_keys:
  key_value_1[i] = test1_result[i]
  key_value_2[i] = test2_result[i]

plot_bar(key_value_1)

plot_bar(key_value_2)

x_pos = np.linspace(0, 9, 41)
barWidth = 0.05
fig = plt.subplots(figsize =(20, 20)) 
common_keys = [ ord(i) for i in common_keys ]

plt.bar(x_pos, list(key_value_1.values()), color ='r', width = barWidth, 
		edgecolor ='grey', label ='aigiri_test1') 
plt.bar(x_pos + barWidth, list(key_value_2.values()), color ='g', width = barWidth, 
		edgecolor ='grey', label ='aigiri_test2') 

plt.xticks(x_pos, common_keys)
plt.legend()
plt.savefig('normalized.png')
plt.savefig('normalized.eps')
plt.show()