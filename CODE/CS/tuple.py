#1.tuple
#********
    1. Creates an empty tuple if no argument is passed
    2. Creates a tuple if a sequence is passed as argument
>>> tuple1 = tuple()
>>> tuple1
( )
>>> tuple1 = tuple('aeiou')#string
>>> tuple1
('a', 'e', 'i', 'o', 'u')
>>> tuple2 = tuple([1,2,3]) #list
>>> tuple2
(1, 2, 3)
>>> tuple3 = tuple(range(5))
>>> tuple3
(0, 1, 2, 3, 4)

#2. count()
#**********
    1. returns the number of times the specified element appears in the tuple.
    2. takes a single parameter
    3. if item not present it returns zero

>>> t=(10,10.0,(10))        # counts the item
>>> t.count(10)
3
>>> t=(10,(10,20),[10,20])
>>> t.count([10,20])      # counts only the list
1
>>> t=(10,'a','A')
>>> t.count('a')            # checks the same case
1
>>> t.count('b')            #if item not present returns zero
0

#3.index()
#**********
    1. returns the index of the specified element in the tuple.
    2. take one to three parameters:
            element - the item to scan
            start_index (optional) - start scanning the element from the start_index
            end_index (optional) - stop scanning the element at the end_index
    3. returns:
            the index of the given element in the tuple
            ValueError exception if the element is not found in the tuple
>>> a=(10,10.0,10.05,'a')
>>> a.index(10)                         # returns the index
0
>>> a=(10,0,'a','ant','A')
>>> a.index('a',2,5)                    # includes the starting value
2
>>> a.index('a',0,2)                    # ending value is not included
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a.index('a',0,2)
ValueError: tuple.index(x): x not in tuple



#4.sorted()
#**********
       1. Takes elements in the tuple and returns a new sorted list.
       2.   It should be noted that, sorted() does not make any change to the original tuple
>>> a=(10,0,'a','ant','A')
>>> b=sorted(a)                         #cannot sort with different datatype
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    b=sorted(a)
TypeError: '<' not supported between instances of 'str' and 'int'
>>> a=(10.5,10.05,10,10.0,10)
>>> b=sorted(a)                         #sorted in ascending
>>> b
[10, 10.0, 10, 10.05, 10.5]
>>> print(sorted(a,reverse=True))       # sorted in descending
[10.5, 10.05, 10, 10.0, 10]


#5.max() 6. min() 7. sum()
#*************************
    1. Returns minimum or smallest element of the tuple
    2. Returns maximum or largest element of the tuple
    3. Returns sum of the elements of the tuple


>>> a=(10.5,10.05,10,10.0,10)
>>> print(max(a))
10.5
>>> print(min(a))
10
>>> print(sum(a))
50.55

>>> a=(10,20,(10,20))
>>> print(max(a[2]))
20
>>> print(min(a[2]))
10
>>> print(sum(a[2]))
30


#*********





    
