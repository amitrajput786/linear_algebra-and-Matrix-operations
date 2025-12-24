
""" solving the problems based on 2d and 3d matrix """"""  date -22 dec """
""" it is based on the problem of creating sub array  for  target sum """


class solution:
    def sub_tar_sum(self, arr, target):
        n=len(arr)
        count=0
        result=[]
        
        for i in range(n):
            c_r=0## here list is not collable
            for j in range(i,n):
                c_r+=arr[j]
                if c_r==target:
                    count+=1
                    result.append(arr[i:j+1])
        return result 
    
    
if __name__=="__main__":
    target=int(input("enter the target sum "))
    arr=list(map(int, input("enter your array").split()))
    s=solution()
    d=s.sub_tar_sum(arr, target)
    print(d)




class solution:
    def d_matrix(self,cols,rows):
        matrix=[]
        for i in range(rows):
            row=[]
            for j in range(cols):
                row.append(0)
            matrix.append(row)
        return matrix
if __name__=="__main__":
    cols=3
    rows=3 
    s=solution()
    d=s.d_matrix(cols,rows)
    print(d)

class solution:
    def matrix_3d(self, cols,row,vector):
        vectors=[]
        for i in range(vector):
            matrix=[]
            for j in range(cols):
                row=[]
                for k in range(rows):
                    row.append(0)
                matrix.append(row)
            vectors.append(matrix)
        return vectors
if __name__=="__main__":
    cols=3 
    vector=3 
    rows=3
    s=solution()
    d=s.matrix_3d(cols, row, vector)
    print(d)
""" now we  are going to lern basic traversal  row- wise , left to right & top to bottom  """ 


class solution:
    def row_wise_traversal(self,matrix):
        cols=len(matrix[0])
        rows=len(matrix)
        d=[]
        for i in range(rows):
            for j in range(cols):
                d.append(matrix[i][i])
        return d
if __name__=="__main__":
    t=int(input("size of input: "))
    matrix=[]
    
    for _ in range(t):
        arr=list(map(int,input("enter the matrix element: ").split()))
        matrix.append(arr)
    s=solution()
    d=s.row_wise_traversal(arr)
    print(matrix)
    print(d)

t= int(input("enter the size of matrix"))
matrix=[]
for _ in range(t):
    arr=list(map(int, input("enter the matrix element ").split()))
    matrix.append(arr)
print(matrix)
""" correct solution """
class Solution:
    def row_wise_traversal(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        d = []

        for i in range(rows):
            for j in range(cols):
                d.append(matrix[i][j])
        return d


if __name__ == "__main__":
    t = int(input("size of input: "))
    matrix = []

    for _ in range(t):
        row = list(map(int, input("enter the matrix element: ").split()))
        matrix.append(row)

    s = Solution()
    d = s.row_wise_traversal(matrix)

    print("Matrix:", matrix)
    print("Row-wise traversal:", d)


""" write the code for column wise traversal , bottom to down """
class solution:
    def col_wise(self, matrix):
        cols=len(matrix[0])
        rows=len(matrix)
        d=[]
        for i in range(cols):
            for j in range(rows):
                d.append(matrix[j][i])
        return d
if __name__=="__main__":
    t=int(input("enter  your input: "))
    matrix=[]
    for _ in range(t):
        arr=list(map(int, input(" enter matrix element: ").split()))
        matrix.append(arr)
    s=solution()
    x=s.col_wise(matrix)
    print("matrix:", matrix)
    print("1D matrix: ", x)
    
""" sum of all the element of the matrix """
class solution:
    def sum_matrix(self,matrix):
        cols=len(matrix[0])
        rows=len(matrix)
        t_r=0
        c_s=[]
        r_s=[]
        for i in range(cols):
            r_r=0
            c_r=0
            for j in range(rows):
                r_r+=matrix[i][j]
                c_r+=matrix[j][i]
                t_r+=matrix[i][j]
            c_s.append(c_r)
            r_s.append(r_r)
        return t_r, c_s,r_s
if __name__=="__main__":
    t=int(input("size of matrix: "))
    matrix=[]
    for _ in range(t):
        arr=list(map(int,input("enter your input").split()))
        matrix.append(arr)
    s=solution()
    x=s.sum_matrix(matrix)
    print("matrix:" , matrix)
    print(" overall sum of matrix , column-wise sum , row-wise sum: ",x)
                
""" matrix addition using numpy """


class solution: 
    def matrix_sum(self,A,B):
        cols=len(A[0])
        rows=len(A)
        result=[]
        for i in range(cols):
            matrix=[]
            for j in range(rows):
                matrix.append(0)
            result.append(matrix)
        
        for i in range(cols):
            for j in range(rows):
                result[i][j]=A[i][j]+B[i][j]
        return result
if __name__=="__main__":
    t=int(input("enter the size fo matrices: "))
    matrix1=[]
    for _ in range(t):
        arr=list(map(int,input("enter your matrix  elements").split()))
        matrix1.append(arr)
    matrix2=[]
    for _ in range(t):
        arr=list(map(int, input("enter your matrix element here : ").split()))
        matrix2.append(arr)
    s=solution()
    x=s.matrix_sum(matrix1,matrix2)
    print("A:",matrix1)
    print("B:",matrix2)
    print("sum-matrix :", x)    
    
    
"""  Multiplication of two matrices """



class solution:
    def matrix_mulitplication(self,A, B):
        row_a=len(A)
        col_a=len(A[0])
        row_b=len(B)
        col_b=len(B[0])
        if col_a!=row_b:
            return "matrix multiplication not possible"
        result=[]
        for i in range(row_a):
            matrix=[]
            for j in range(col_b):
                matrix.append(0)
            result.append(matrix)
        for i in range(row_a):
            
            for j in  range(col_b):
                
                
                for k in range(col_a):
                    result[i][j]+=A[i][k]*B[k][j]
        return result
if __name__=="__main__":
    t=int(input("enter the row of A: "))
    matrix1=[]
    for _ in range(t):
        arr=list(map(int,input("enter the  element of A: ").split()))
        matrix1.append(arr)
    t1=int(input("enter the row of B: "))
    matrix2=[]
    for _ in range(t1):
        arr=list(map(int, input("enter the element of matrix2: ").split()))
        matrix2.append(arr)
    s=solution()
    c=s.matrix_mulitplication(matrix1, matrix2)
    print("matrix1:", matrix1)
    print("matrix2;",matrix2)
    
    print("multiplication_result: ", c)
    
    
    
""" transpose of the matrix """
class solution:
    def transpose(self,A):
        row_a=len(A)
        col_a=len(A[0])
        result=[]
        for i in range(col_a):
            matrix=[]
            for j in range(row_a):
                matrix.append(0)
            result.append(matrix)
        for i in range(row_a):
            for j in range(col_a):
                result[j][i]=A[i][j]
        return result
if __name__=="__main__":
    t=int(input("enter the no. of rows"))
    matrix=[]
    for _ in range(t):
        arr=list(map(int, input("enter the element: ").split()))
        matrix.append(arr)
    s=solution()
    x=s.transpose(matrix)
    print("input matrix: ", matrix)
    print("trans-pose matrix: ", x)
    
"""  write the code  to calculate the sum of the both diagonal of the matrix """
"""Indices: [0][2], [1][1], [2][0]
Pattern: i + j == n - 1"""
class solution:
    def diagonal_sum(self, A):
        row=len(A)
        col=len(A[0])
        if row!=col:
            return " not a square matrix"
        c=0
        d=0
        for i in range(row):
            
            c+=A[i][i]
            d+=A[i][row-1-i]
        return c+d , c ,d
if __name__=="__main__":
    t=int(input("enter the row"))
    matrix1=[]
    for _ in range(t):
        arr=list(map(int, input("enter the input").split()))
        matrix1.append(arr)
    s=solution()
    x=s.diagonal_sum(matrix1)
    print("input matrix: ", matrix1)
    print("diagonal sum: ", x)
    