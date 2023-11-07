zxc = 0
for a in range(1,10):
    for b in range(1,10):
        zxc+=1
        print(b*a, end = ' ')
        if zxc%9==0:
            print(end = '\n')