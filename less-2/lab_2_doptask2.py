z=int(input())
x=int(input())
c=int(input())
if z+x<=c or x+c<=z or z+c<=x:
    print('нельзя')
else:
    if z==x or c==z or c==x:
        if z==x and x==c:
            print('равностороний')
        else:
            print('равнобедренный')
    else:
        print('неравнобедренный')