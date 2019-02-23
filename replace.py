import re
string = 'AAAABAABAABABAA'
lines = ['AA','BB']
count = len(re.findall('(?=AA)', string))
search = '(?='+lines[0]+')'
s = [m.start() for m in re.finditer(search, string)]

for i in range(len(s)):
    print(string[:s[i]] + lines[1] + string[s[i]+2:])
print(count, s)
