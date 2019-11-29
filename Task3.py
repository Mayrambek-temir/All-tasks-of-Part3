st = input('input num to list: ')
print(st)
l=list(st.replace(' ', ''))
print(l)

num=int(input('skolko raz sdvinut: '))
while num:
    pop_=l.pop()
    l.insert(0,pop_)
    num-=1
print(l)
