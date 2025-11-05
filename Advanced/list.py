import math
def reverse(l,s,e):
    while s<e:
        l[s], l[e] = l[e], l[s]
        s = s+1
        e = e-1

#1 Left rotate an array by d places
def rotate_by_d(l,d):
    # return l[d:] + l[ :d] -> inbuilt
    reverse(l, 0, d-1)
    reverse(l, d, len(l)-1)
    reverse(l, 0, len(l)-1)
    return l

#Time Comp = O(n)

#2 MAx difference in an array where i<j, max(arr[j] - arr[i])
def naive_max_difference(l):
    res = l[1]-l[0]
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            res = max(l[j]-l[i],res)
    return res
#Time Comp = O(n*n)

def max_difference(l):
    min_val = l[0]
    res = l[1]-l[0]
    for i in range(1,len(l)):
        res = max(res,l[i]-min_val)
        min_val = min(min_val,l[i])
    return min_val
#Time Comp = O(n)
    
#3 Max profit in stock buy and sell
def own_stock_buy_sell(l):
    res = 0
    stock_buy = l[0]
    stock_sell = l[0]
    for i in range(1,len(l)):
        if l[i]>stock_sell:
            stock_sell = l[i]
        else:
            res += (stock_sell - stock_buy)
            stock_buy = l[i]
            stock_sell = l[i]
    res += (stock_sell - stock_buy)
    return res

def naive_stock_buy_sell(l,s,e):
    if s>=e:
        return 0
    res = 0
    for i in range(s,e):
        for j in range(i+1,e+1):
            if l[j]>l[i]:
                curr_res = l[j]-l[i] + naive_stock_buy_sell(s,i-1) + naive_stock_buy_sell(j+1,e)
                res = max(res,curr_res)
    return res

def stock_buy_sell(l):
    profit = 0
    for i in range(1,len(l)):
        if l[i]>l[i-1]:
            profit += l[i]-l[i-1]
    return profit
#Time Comp = O(n)

#3 Trapping rain water
def naive_trapping_rain_water(l):
    res = 0
    for i in range(1,len(l)-1):
        lmax = l[i]
        for j in range(i):
            lmax = max(lmax,l[j])
        rmax = l[i]
        for j in range(i+1,len(l)):
            rmax = max(rmax,l[j])
        res += (min(lmax,rmax)-l[i])
    return 
#Time Comp = O(n*n)

def trapping_rain_water(l):
    res = 0
    lmax=[0]*len(l)
    rmax=[0]*len(l)
    lmax[0] = l[0]
    for i in range(1,len(l)):
        lmax[i] = max(l[i],lmax[i-1])
    rmax[len(l)-1]=l[len(l)-1]
    for i in range(len(l)-2,-1,-1):
        rmax[i] = max(l[i],rmax[i+1])
    for i in range(1,len(l)-1):
        res += (min(lmax[i],rmax[i])-l[i])
    return res
#Time Comp = O(n), AuxSpace = O(n)

#4 Maximum Subarray SUm
def naive_max_subarray_sum(l):
    max_sum = l[0]
    for i in range(len(l)):
        curr_sum = 0
        for j in range(i,len(l)):
            curr_sum += l[j]
            max_sum = max(max_sum,curr_sum)
    return max_sum
#Time Comp = O(n*n)

def max_subarray_sum(l):  #Kadane's Algorithm
    curr_sum = l[0]
    max_sum = l[0]
    for i in range(i,len(l)):
        curr_sum = max(curr_sum+l[i],l[i])
        max_sum = max(max_sum,curr_sum)
    return max_sum
#Time Comp = O(n)

#5  Maximum length of even odd subarray
def naive_max_length_even_odd_subarray(l):
    max_count = 1
    for i in range(len(l)):
        count = 1
        for j in range(i+1,len(l)):
            if (l[j-1]%2==0 and l[j]%2==1) or (l[j-1]%2==1 and l[j]%2==0):
                count += 1
            else:
                break
        max_count = max(max_count,count)
    return max_count
#Time Comp = O(n*n)

def max_lenght_even_odd_subarray(l):
    mod_2 = l[0]%2
    count = 1
    res = 1
    for i in range(1,len(l)):
        if l[i]%2!=mod_2:
            count += 1
            res = max(count,res)
        else:
            count = 1
        mod_2 = l[i]%2
    return res
#Time Comp = O(n)

#6 Maximum circular sub array sum
def naive_max_circular_subarray_sum(l):
    res = l[0]
    for i in range(len(l)):
        curr_sum = l[i]
        max_sum = l[i]
        for j in range(i+1,len(l)):
            ind = (i+j)%len(l)
            curr_sum = max(curr_sum+l[ind], l[ind])
            max_sum = max(max_sum,curr_sum)
        res = max(max_sum,res)
    return res
#Time Comp = O(n*n)



def max_circular_subarray_sum(l):
    total_sum = l[0]  # Total sum of array
    curr_max_sum = l[0]  # Kadane’s max subarray sum
    max_sum = l[0]
    curr_min_sum = l[0]  # Kadane’s min subarray sum
    min_sum = l[0]

    for i in range(1, len(l)):
        curr_max_sum = max(curr_max_sum + l[i], l[i])
        max_sum = max(max_sum, curr_max_sum)

        curr_min_sum = min(curr_min_sum + l[i], l[i])
        min_sum = min(min_sum, curr_min_sum)

        total_sum += l[i]

    # Handle case when all elements are negative
    if total_sum == min_sum:
        return max_sum

    return max(max_sum, total_sum - min_sum)
#Time Comp = O(n)


#7  Majority element in an array, element appearing more than n//2 times
def naive_majority(l):
    for i in range(len(l)):
        count = 1
        for j in range(i+1,len(l)):
            if l[i] == l[j]:
                count += 1
        if count> len(l)/2:
            return i
    return -1
#Time Comp = O(n*n)

def majority_element(l):
    res = 0
    count = 1
    for i in range(1,len(l)):
        if l[res]==l[i]:
            count += 1
        else:
            count -= 1
        if count==0:
            res = i
            count = 1
    if l.count(l[res]) > len(l)//2:
        return res
    return -1
#Time Comp = O(n)
    
#8 Minimum group flips to make a binary array homogenous
def minimum_group_flips(l):
    for i in range(1,len(l)):
        if l[i]!=l[i-1]:
            if l[i]!=l[0]:
                print('From',i,'to',end=" ")
            else:
                print(i-1)
    if l[len(l)-1]!=l[0]:
        print(len(l)-1)
#Time Comp = O(n)

#9 Max sum of K consecutive elemenst ;                    
def naive_max_k_cons_sum(l,k):
    max_sum = -math.inf
    for i in range(len(l)-k+1):
        sum = 0
        for j in range(i,i+k):
            sum += l[j]
        max_sum = max(max_sum,sum)
    return max_sum
#TimeComp = O(nk)

def max_k_cons_sum(l,k):                                  #sliding window technique
    sum = 0
    for i in range(k):
        sum += l[i]
    max_sum = sum
    for i in range(1,len(l)-k+1):
        sum = sum-l[i-1]+l[i+k-1]
        max_sum = max(max_sum,sum)
    return max_sum

#Time COmp = O(n)
    
#10 Subarray with given sum                       

def naive_subarray_given_sum(l,s):
    for i in range(len(l)):
        curr_sum = 0
        for j in range(i,len(l)):
            curr_sum += l[i]
            if curr_sum == s:
                return True
    return False
#Time COmp = O(n*n)

def subarray_given_sum(l,s):                   # Dynamic sliding Window technique
    s, curr_sum = 0
    for e in range(len(l)):
        curr_sum += l[e]
        while (curr_sum>s):
            curr_sum -= l[s]
            s+= 1
        if(curr_sum==s):
            return True
    return False
#Time COmp = O(n)

#11 Prefix Sum Technique

def prefix_sum_tq(l,s,e):
    arr = [0]*len(l)
    arr[0] = l[0]
    for i in range(1,len(l)):
        arr[i] = arr[i-1] + l[i]
    
    if s == 0:
        return arr[e]
    else:
        return arr[e]-arr[s-1] 
#Time COmp = O(n)

#12 Equilibrium point

def equilibrium(l):
    right_sum = 0
    left_sum = 0
    for i in range(0,len(l)):
        right_sum += l[i]
    
    for i in range(len(l)):
        right_sum -= l[i]
        if left_sum == right_sum:
            return True
        left_sum += l[i]
    return 
#Time COmp = O(n)

#13 3 partitions with equal sum

def three_partition_with_equal_sum(l):
    if sum(l)%3!=0:
        return False
    partition_sum = sum(l)/3
    curr_sum = 0
    count = 0
    for i in range(len(l)):
        curr_sum += l[i]
        if curr_sum==partition_sum:
            count += 1
            curr_sum=0
        if count==2:
            return True
    return False
#Time COmp = O(n)

#14 Maximum appearing element in ranges ; constraints: 0<=left[i]<=right[i]<100

def naive_max_ele(left,right):
    freq = [0]*100
    for i in range(len(left)):
        for j in range(left[i],right[i]+1):
            freq[j] += 1
    
    return freq.index(max(freq))

#TimeComp = O(100*n), Aux Space = O(1)

def max_ele(left,right):
    freq = [0]*101
    for i in range(len(left)):
        freq[left[i]] += 1
        freq[right[i]+1] -= 1
    
    for i in range(1,100):
        freq[i] += freq[i-1] 

    return freq.index(max(freq))

#Time COmp = O(n)  

#15 Smallest missing positive number

def missingNumber(self,arr):
        #Your code here
    l = arr
    for i in range(len(l)):
        while 1<=l[i]<=len(l) and l[l[i]-1]!= l[i]:
            temp = l[i]                                            # Avoid Mutation - if we directly swap l[i], l[l[i]-1] then l[i] can change during the swap, and the next part of the expression (l[l[i]-1]) might be indexing the wrong thing. One mutation breaks multiple assumptions. So store l[i] value in a temp var``
            l[i], l[temp-1] = l[temp-1], l[i]
        
    for i in range(len(l)):
        if l[i]!=i+1:
            return i+1
    return len(l)+1
# TimeComp = O(n) Space Comp = O(1)


#16    Function to rearrange an array so that arr[i] becomes arr[arr[i]] with O(1) extra space.
def arrange(self,arr, n): 
    #Your code 
    for i in range(len(arr)):
        arr[i] += (arr[arr[i]]%n)*n
            
    for i in range(len(arr)):
        arr[i] = arr[i]//n


#17 Given an array arr of positive integers. The task is to return the maximum of j - i subjected to the constraint of arr[i] < arr[j] and i < j.
#Logic: Because lmin is non-increasing from left to right (never goes up), and rmax is non-decreasing from right to left (never goes down).

'''
You want to find the farthest j > i such that arr[j] > arr[i].
But this takes too long if you check every cell.

So instead:

You create a path that moves intelligently — like a “sliding window” or “two-pointer scan.”

If the current rmax[j] >= lmin[i], it might be a valid answer → check j - i.

Then move j to the right (to try a larger window).

Else, if it fails, move i to the right to find a smaller lmin.

So you're always trying to stretch the window (j - i) as far as you can, only backing off if the condition arr[j] > arr[i] fails.

'''
def maxIndexDiff(self, arr):
    # code here
    lmin = [0]*len(arr)
    lmin[0] = arr[0]
    for  i in range(1,len(arr)):
        lmin[i] = min(lmin[i-1],arr[i])
        
    rmax = [0]*len(arr)
    rmax[len(arr)-1] = arr[len(arr)-1]
    for i in range(len(arr)-2,-1,-1):
        rmax[i] = max(rmax[i+1],arr[i])
        
    res = 0
    i, j = 0, 0
    while i<len(lmin) and j<len(rmax):
        if lmin[i]<=rmax[j]:
            res = max(res, j-i)
            j += 1
        else:
            i += 1
    return res


'''
Important array Techniques:
-> Two Pointer approach 
(Working with sorted arrays
Finding pairs with a certain condition (like sum)
Searching in a contiguous subarray (sliding window flavor)
Reversing or comparing strings/arrays
Merging things (like merge sort))
One pointer at start and the other at end
Both pointers at start with one moving by for loop, while the other one gets updated based on conditions

-> Sliding Window

-> Dynamic Sliding Window

-> Precomputing  (Prefix Sum/ Lmax / Rmax/ Lmin / Rmin)

-> Kadane's Algo

-> Hashing technique

-> Binary search (works best for sorted and eliminating one half of the range)

'''
 
    
