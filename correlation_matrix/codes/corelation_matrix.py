import pandas as pd
import numpy as np

stothram_file = open('aigiri.txt', 'r')
stothram_txt = stothram_file.read()
stothram_file.close()

slokams = []
for sloka in stothram_txt.split('||'):
  if not sloka.replace(' ', '').isnumeric() and not sloka == '\n':
    slokams.append( sloka.replace('|', '').replace('\n', '') )

correlation_dict = {}

for index, sloka in enumerate(slokams):
  temp = []
  for words in sloka.split(' '):
    for char in words:
      temp.append(ord(char))
  correlation_dict[ str(index + 1) ] = np.array(temp)

length = [ len(char_array) for char_array in correlation_dict.values() ]
max_length = max(length)

for key in correlation_dict:
  correlation_dict[key] = np.pad(correlation_dict[key], (0, max_length - len(correlation_dict[key])), 'constant')

df = pd.DataFrame( correlation_dict )
corrMatrix = df.corr()
corrMatrix.to_excel("corrMatrix.xlsx")