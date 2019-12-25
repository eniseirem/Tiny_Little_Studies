#!/usr/bin/env python
# coding: utf-8

n=8 
dis=1 
layers=3
space=n+(n/2)+layers

print('\033[31m' + 'Merry Christmas!' + '\033[0m')  # Red text


for level in range(0,3):
    for i in range(0,n):
        for k in range(i,int(space)):
            print("\033[32m"+" ",end='')
            
        for j in range(0,(i+dis)):
            if(j%2==0) and ((i%2==0) or (i%2==1)):
                if(i==0) and (j==0) and (level==0):
                    print('\033[1;37m' + 'X' + '\033[0;0m',end='')
                elif(j==0) and (i%2==1):
                    print("\033[32m"+"/",end='')
                elif(i%2==1) and (dis%2==0) and (j==(dis+i-1)):
                    print("\\",end='')
                else:
                    if j==0 or (j%4==0 and (j+dis)%3==2):
                        #asal(i+j+dis)==True or
                        print('\033[33m' + '@' + '\033[0m', end='')
                    elif(j%4==0 and (j+dis)%3==1):
                        print('\033[31m' + '&' + '\033[0m', end='') 
                    else:
                        print("\033[32m"+"*", end='')
            else:
                print("\033[32m" +".",end='')
        
        dis= dis+1
        print(" ")
        
    space=space-(n/2)
    
for i in range(0,5):
    for k in range(0,(n+layers)):
        print(" ",end='')
    for j in range(0,2):
        print("\033[30m |#|",end='')
        
    print()

                




