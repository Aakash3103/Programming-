# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 17:42:29 2021

@author: aakas
"""

def rotate(arr,d,num):
    if (d==0 or d==num):
        print("same output :-",arr)
    else:
        arr2=arr[d-1::-1]
        arr2[3:]=arr[num:d-1:-1]
        arr2=arr2[::-1]
        return arr2;
    
if __name__=='__main__':
    arr= []
    num = int(input("enters the numbers in the list :"))
    d = int(input("enter the number do you want to reverse : "))
    for i in range(0,num):
        ele = int(input())
        arr.append(ele) 
prnt = rotate(arr,d,num)
print(prnt)