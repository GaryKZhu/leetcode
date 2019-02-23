import re

string = 'AAAABAABAABABAA'
lines = ['AA','BB']
def replace(replace,sub,string): #Replace = thing to replace, Sub = thing to sub in, string = input string
    count = len(re.findall('(?=AA)', string))   
    search = '(?='+replace+')'
    s = [m.start() for m in re.finditer(search, string)]
    output = []
    for i in range(len(s)):
       output.append(string[:s[i]] + sub + string[s[i]+2:])
    return '\n'.join(output)

print(replace(lines[0], lines[1], string))
