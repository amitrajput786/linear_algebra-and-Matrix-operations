#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 21:15:07 2025

@author: amit
"""

""" code to find out the maximum subarray for the possible sum"""
class solution:
    def sum_sub(arr,k):
        n=len(arr)
        result=[]
        count=0
        for i in range(n):
            c_r=0
            for j in range(i,n):
                c_r=+arr[j]
                if c_r==k:
                    count+=1
                    result.append(arr)
        return result
if __name__=="__main__":
    t=int(input("enter the target sum: "))
    c=list(map(int, input("enter the array element: ").split()))
    s=solution()
    x=s.sum_sub(c,t)
    print("input array; ",c)
    print("result: ", x)


""" code to find out  possible subarray for the targeted product """
class solution:
    def sub_product(self,arr,p):
        n=len(arr)
        result=[]
        count=0
        for i in range(n):
            c_r=1
            for j in range(i,n):
                c_r*=arr[j]
                if c_r==p:
                    count+=1
                    result.append(arr[i:j+1])
        return result, count
if __name__=="__main__":
    t=int(input("enter the targeted multiple: "))
    arr=list(map(int, input("enter the array: ").split()))
    s=solution()
    x=s.sub_product(arr, t)
    print("input arr: ",arr)
    print("resultant subaaray: ",x )
    
    
"""  code to find the possible  subarray to find the targeted average """

class solution:
    def sub_avg(self,arr,avg):
        n=len(arr)
        result=[]
        count=0
        for i in range(n):
            c_r=0
            c_d=0
            for j in range(i,n):
                c_r+=arr[j]
                c_d+=1
                x=c_r/c_d
                if x==avg:
                    count+=1
                    result.append(arr[i:j+1])
        return result, count
if __name__=="__main__":
    t=int(input("enter the target average: "))
    arr=list(map(int, input("enter the element of arr: ").split()))
    s=solution()
    x=s.sub_avg(arr, t)
    print("input matrix: ", t)
    print(" resultant subarray:",x)
    
                