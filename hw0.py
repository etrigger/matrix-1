# Please fill out this stencil and submit using the provided submission script.





## Problem 1
def myFilter(L, num): return [ x for x in L if x%num !=0 ]



## Problem 2
def myLists(L): return [ list(range(1,x+1)) for x in L  ]



## Problem 3
def myFunctionComposition(f, g): return { x:g[f[x]] for x in f.keys()  }


## Problem 4
# Please only enter your numerical solution.

complex_addition_a = (3+1j)+(2+2j) 
complex_addition_b = (-1+2j)+(1-1j)
complex_addition_c = (2+0j)+(-3+.001j)
complex_addition_d = 4*(0+2j)+(.001+1j)



## Problem 5
GF2_sum_1 = 1
GF2_sum_2 = 0
GF2_sum_3 = 0


## Problem 6
def mySum(L): 
    current = 0
    for x in L:
        current =  current + x
    return current



## Problem 7
def myProduct(L): 
    current = 1
    for x in L:
        current =  current*x
    return current



## Problem 8
def myMin(L):
    min = L[0]
    for i in L:
        if i<min: min = i
    return min



## Problem 9
def myConcat(L):
    string = str()
    for i in L:
        string = string + str(i)
    return string   



## Problem 10
def myUnion(L):
    union = set()
    for i in L:
        union = union | i
    return union

