s = input('Enter string')
s = s.split()
s.sort(key=len)
s = " ".join(s)
print(s)
