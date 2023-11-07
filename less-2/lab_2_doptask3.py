z=int(input(''))
x=1
c=''
while x != 0:
    x=z//10
    c+=str(z%10)
    z=x
print(c)