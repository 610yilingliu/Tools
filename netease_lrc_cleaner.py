import re

infile = input('Input File Name or Path: ')

with open(infile, 'rb') as f:
    contents = f.read()

# if error, please change your decode pattern to utf8 or somethings else (base on your lyrics encoding)
contents = contents.decode('gbk')

pattern = re.compile(r'\[00:00(.*?)(?="},)')
res = re.search(pattern, contents)
lrc = res.group()
a = lrc.replace(r'\n', '\n')
with open(infile, 'w') as f:
    f.write(a)

print('Finished')