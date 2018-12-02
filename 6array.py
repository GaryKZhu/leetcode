numRow = 4
s = "PAYPALISHIRING"
numColumn = len(s)
row = [[' ' for x in range(numRow)] for y in range(numColumn)]
sequencerow = 1
sequencecolumn = 0
indexrow = 0
indexcolumn = 0
for x in s:
    row[indexcolumn][indexrow] = x
    if indexrow == numRow - 1:
        sequencerow = -1
        sequencecolumn = 1
    if indexrow == 0:
        sequencerow = 1
        sequencecolumn = 0
    indexrow = indexrow + sequencerow
    indexcolumn = indexcolumn + sequencecolumn

for i in row:
    if i==[' ']:
       row.remove(i)

rotated = list(zip(*(row)))

for list in row:
    print('  '.join(list))
    
for list in rotated:
    print('  '.join(list))

