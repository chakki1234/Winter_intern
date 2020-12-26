unicode_txt = open('unicode.txt', 'r')
u_txt = unicode_txt.read()
unicode_txt.close()

u_char = u_txt.split()
checked_u_char = []
periodicity = {}

def to_cal_periodicity(i, index):
    count = 0
    temp = u_char[index+1:]
    for j in temp:
        if j == i:
            periodicity[i].append(count)
            count = 0
        else:
            count = count + 1


for j, i in enumerate(u_char):
    if i in checked_u_char:
        pass
    else:
        checked_u_char.append(i)
        periodicity[i] = []
        to_cal_periodicity(i, j)

print(periodicity)