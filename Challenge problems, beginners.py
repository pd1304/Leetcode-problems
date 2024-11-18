# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 16:11:42 2024

@author: pareshdokka
"""

## LEETCODE QUESTIONS 1 ##

#1480. given an array, return an array wchich cumulatively sums the integers in the array


def solution(nums):
    lists = []
    for i in range(0,len(nums)+1): # [0-len(nums)] will only give upto the last i, not including
        j = sum(nums[0:i])
        lists.append(j)
    return lists[1:] # skips the first row, and gives a list of the rest

print(solution([1,2,3,4,5]))

#1672: Richest customer wealth: Given a 2d matrix, with people
#and the moeny they have in each bank, find the person with max money

'''
def maximumWealth(accounts):
        max_sum = 0
        for row in accounts:
            account_sum = 0
            for column in row:
                account_sum += column
            if account_sum> max_sum:
                max_sum = account_sum
        return max_sum        
'''


#412. FIZZ BUZZ: Given an integer, produce an array
# where if n is divisible by 3 - Fuzz
# where if n is divisible by 5 - Buzz
# where if n is divisible by both - FIZZBUZZ
'''
def fizzbuzz(n):
    num_list = []
    for i in range(0,n+1):
        num_list.append(str(i))
        
        if i%3==0 and i%5==0:
            num_list[i] = 'FizzBuzz'
        elif i%3 == 0:
            num_list[i] = 'Fizz'
        elif i%5 == 0:
            num_list[i] = 'Buzz'
            
    return num_list[1:]

print(fizzbuzz(15))
'''

#1342. No. of steps to 0. Given an integer, divide it by 2, or subtract by 1,
# to get to 0, and return the no of steps it took to get to 0.

'''
def stepstoserzo(n):
    steps = 0
    while n>0:
        if n%2 == 0:
            n = n/2
            steps += 1
        else:
            n = n-1
            steps += 1
    return steps

print(stepstoserzo(6))

'''        




