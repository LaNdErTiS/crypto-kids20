import chardet

numbers = [21328, 16963, 21574, 24402, 12621, 30005, 24390, 12596, 18293, 13663, 18483, 21043, 12597] # got from link

rez = b''
for i in numbers:
    rez += i.to_bytes(2, byteorder='big')

the_encoding = chardet.detect(rez)['encoding']

print(the_encoding)
print(rez)
