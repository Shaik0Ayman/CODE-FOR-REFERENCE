# text file 
'''f = open('txtfie.txt', 'w')
data = 'hellow blah'
f.write(data)
'''
with open('txtfie.txt', 'w') as f:
    f.writelines(['hello', 'world'])

