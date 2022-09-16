x=int(input('enter no='))
i=1
while i<=x:
    if i==1:
        print('    *'*i)
    elif i==x:
        print('* '*i)
    else:
        print(' '*(x-i)+'*'+' '*(2*i-3)+'*')
    i=i+1

