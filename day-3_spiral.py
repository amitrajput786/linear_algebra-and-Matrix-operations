#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 27 16:35:06 2025

@author: amit
"""
""" row-wise traversal  on given matrix"""
class solution:
    def row_wise(self,matrix):
        row=len(matrix)
        col=len(matrix[0])
        d=[]
        for i in range(row):
            
            for j in range(col):
                
                d.append(matrix[i][j])
        return d
if __name__=="__main__":
    t=int(input("enter the no. of rows"))
    matrix=[]
    for _ in range(t):
        arr=list(map(int,input("enter the matrix element").split()))
        matrix.append(arr)
    s=solution()
    x=s.row_wise(matrix)
    print("input matrix:", matrix)
    print("row-wise traversal: ",x)

""" column-wise traversal on given matrix """
class solution:
    def col_wise(self,matrix):
        row=len(matrix)
        col=len(matrix[0])
        d=[]
        for i in range(col):
            for j in range(row):
                d.append(matrix[j][i])
        return d 
if __name__=="__main__":
    t=int(input(" enter the row of matrix "))
    matrix=[]
    for _ in range(t):
        arr=list(map(int,input("enter the matrix element ").split()))
        matrix.append(arr)
    s=solution()
    v=s.col_wise(matrix)
    print("intput matirx: ", matrix)
    print("col-wise: ", v)
    
""" sum of all the matrix element """
class solution:
    def matrix_sum(self,matrix):
        col=len(matrix[0])
        row=len(matrix)
        d=0
        for i in range(row):
            for j in range(col):
                d+=matrix[i][j]
        return d
if __name__=="__main__":
    t=int(input("enter the rows : "))
    matrix=[]
    for _ in range(t):
        arr=list(map(int, input("enter the matrix :").split()))
        matrix.append(arr)
    s=solution()
    v=s.matrix_sum(matrix)
    print("input matrix:",matrix)
    print("sum of matrix:",v)
    
    
"""  code for the matrix multiplication """
class solution:
    def matrix_muliplication(self,A,B):
        col_a=len(A[0])
        row_a=len(A)
        row_b=len(B)
        col_b=len(B[0])
        if col_a!=row_b:
            return "matrix multiplication not possible"
        result=[]
        for i in range(row_a):
            matrix=[]
            for  j in range(col_b):
                matrix.append(0)
            result.append(matrix)
        for i in range(row_a):
            for j in range(col_b):
                for k in range(col_a):
                    result[i][j]+=A[i][k]*B[k][j]
        return result
if __name__=="__main__":
    t=int(input("enter the rows"))
    A=[]
    for _ in range(t):
        arr=list(map(int,input("enter the row elements").split()))
        A.append(arr)
    B=[]
    t=int(input(" enter the rows of b:"))
    for _ in range(t):
        arr=list(map(int,input("enter the row element: ").split()))
        B.append(arr)
    
    s=solution()
    v=s.matrix_muliplication(A, B)
    print("input matrix A:",A)
    print("input matrix B:",B)
    print("multiple of matrix",v)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
