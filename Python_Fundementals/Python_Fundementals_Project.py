## 1- Write a function that flattens a list. Its elements can consist of multi-layered lists (such as [[3],2]) or non-scalar data. For example:
## input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
## output: [1,'a','cat',2,3,'dog',4,5]
def flatten(x):
    K=[]
    for a in x:
        if type(a)==list:
            K.extend(flatten(a))
        else:
            K.append(a)
    return K

t = flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5])
print(t)

## 2- Write a function that reverses the elements in the given list. If the elements inside the list also contain the list, reverse their elements as well. For example:
## input: [[1, 2], [3, 4], [5, 6, 7]]
## output: [[[7, 6, 5], [4, 3], [2, 1]]


def rev(x):
    x.reverse()
    for a in x:
        if isinstance(a,list):
            rev(a)
            
    return x
print(rev([[1, 2], [3, 4], [5, 6, 7]]))

