#5x3 models
#last character always new line
import re
#row1 = '0   '
#row1 = re.sub('\s',re.escape('\s'), row1)
#row1 = row1 + '\\n'
#print(row1)

emptyRow = 4*' '+'\\n'

row1 = '0   '
row2 = '|   '
row3 = '|   '


model = [row1, row2, row3]
print(''.join(model))