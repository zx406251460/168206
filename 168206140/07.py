L = ['A','B','C','D']
print ("小偷是：")
for i in L:
        s = i
        A = (i != 'A')
        B = (i == 'D')
        C = (i == 'B')
        D = (i != 'D')
        if (A + B + C + D ==1):
                print(i)
