# -*- coding: utf-8 -*-
"""
Spyder Editor

Insertion sort program
"""
import math

def insertion_sort(list):
    for j in range(1, len(list) ) :
        temp = list[j]
        pos = -1
        for i in range(j-1, -1 , -1 ) :
            if list[i] > temp :
                list[i+1] = list[i]
                pos = i
            else:
                pos = i +1
                break
        list[pos] = temp
 
def merge(list, beg, mid,end ) :
    newList = []
    left = beg
    right = mid+1
    
    while left < mid+1 and right < end+1 :
        if list[left] <= list[right] :
            newList.append(list[left])
            left += 1
        else:
            newList.append(list[right])
            right += 1
    
    if left!=mid+1 :
        for i in range(left,mid+1):
            newList.append(list[i])
    elif right != end+1:
        for i in range(right,end+1):
            newList.append(list[i])
            
    list[beg:end+1] = newList
       
def merge_sort(list,beg,end):
    if beg < end:
        mid = int(math.floor((beg + end)/2))
        merge_sort(list,beg,mid)
        merge_sort(list,mid+1,end)
        merge(list, beg, mid, end)
    
def show_list(list):
    for i in range(len(list)):
        print(list[i])
        
list= [5,3,2,4,1]
#insertion_sort(list)
merge_sort(list,0,len(list)-1)
show_list(list)