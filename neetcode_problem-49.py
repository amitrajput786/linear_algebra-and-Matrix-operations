#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 16 19:57:08 2026

@author: amit
"""

""" problems inspired from  the group of anagrams 

Given an array of strings strs, group the together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

    There is no string in strs that can be rearranged to form "bat".
    The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
    The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

"""
from collections import defaultdict

## code 
class solution:
    def anagrams(self,strs):
        res=defaultdict(list)
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord("a")]+=1
            res[tuple(count)].append(s)
        return list(res.values())
if __name__=="__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    s=solution()
    c=s.anagrams(strs)
    print(c)


"""
Problem 1: Group Isomorphic Strings

Description: Group strings that follow the same character pattern.

Example:

    Input: ["egg", "add", "foo", "bar", "cfc", "gzg"]
    Output: [["egg", "add", "foo"], ["bar"], ["cfc", "gzg"]]
    Why? "egg", "add", "foo" all follow pattern (0,1,1) - first char different from next two same chars

"""
class Solution:
    def groupiso(self,strs):
        res=defaultdict(list)
        for s in strs:
            pattern=[]
            char_map={}
            index=0
            for c in s:
                if c not in  char_map:
                    char_map[c]=index
                    index+=1
                    pattern.append(char_map[c])
            res[tuple(pattern)].append(s)
        return list[res.values()], print(pattern)
if __name__ == "__main__":
    sol=Solution()
    x=["egg", "add", "foo", "bar", "cfc", "gzg"]
    c=sol.groupiso(x)
    print(c)
            

