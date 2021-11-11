s=input()

for i in range(1,len(s)//10+1):
    print(s[10*(i-1):10*i])
if(len(s)%10>0):
    print(s[(len(s)//10)*10:])