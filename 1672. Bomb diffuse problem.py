# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 10:57:51 2024

@author: pareshdokka
"""


'''
for k>0:
    let code = [5,7,1,4] k = 3
    we append code with code[:k]
    
    code = [5,7,1,4]+[5,7,1]
    code = [5,7,1,4,4,7,1]
    
    Now we do sliding backward
    
    res = [0,0,0,0]
    
    begin with the last cell:
        
    res[3] = sum(code[0:3]) = 5+7+1 =  13
    res[2] = (4+5+7) = res[3]+code[3]-code[2/6] = 13+4-1 = 16
    res[1] = (1+4+5) = res[2]+code[2]-code[1/5] = 16+1-7 = 10
    res[0] = (7+1+4) = res[1]+code[1]-code[0/4] = 10+7-5 = 12
    
    res[i] = (.. ..) = res[i+1]+code[i+1]-code[i/ (i+k+1)]
    THIS IS THE MAIN EQ

for k>0:
    let code = [2,4,9,3] k = -2
    we append code with code[k:]
    
    code = [9,3]+[2,4,9,3]
    
    code = [9,3,2,4,9,3]
    
    Now we do sliding window forward:
    res = [0,0,0,0]
    res[0] = 9+3 = 12
    res[1] = (2+3) = res[0]-code[0/4]+code[2] = 12-9+2 = 5
    res[2] = (2+4) = res[1]-code[1/5]+code[3] = 5-3+4 = 6
    res[3] = (4+9) = res[2]-code[2]+code[4/0] = 6-2+9 = 13
    
    res[i] = ()    = res[i-1]-code[i-1]+code[i-k-1]  #i-k-1 = i-(-2)-1 = i+1
             
    
    
    
'''
def decrypt(code,k):
    n = len(code)
    if k == 0:
        return[0]*n
    res = [0]*n
    
    if k>0:
        code += code[:k] # [5,7,1,4,5,7,1]
        for i in range(n-1, -1, -1):  # i = n-1,n-2,..., 2,1,0,: python index starts from 0
            if i == n-1:
                res[i] = sum(code[i+1:]) # sum of all the items in code
            else:
                res[i] = res[i+1]+code[i+1]-code[i+k+1] 
                # in the case of res[n-2]: res[n-1]+ code[n-1]-code[]
        return res
    
    if k<0:
        code = code[k:]+code
        for i in range(n):
            if i == 0:
                res[i] = sum(code[:-k])
            else:
                res[i] = res[i-1]+code[i-1-k]-code[i-1]
                
        return res

        
print(decrypt([5,7,1,4],4))            