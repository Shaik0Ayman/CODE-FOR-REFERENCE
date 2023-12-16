'''list():
##########
       1. constructor returns a list in Python.
       2. takes a single argument:
          iterable (optional) - an object that could be a sequence (string, tuples, dictionary)
       3. If no parameters are passed, it returns an empty list
#Example:
>>> a="text:"
>>> k=list(a)                            # passing string
>>> k
['t', 'e', 'x', 't', ':']
>>> k=list(input())
"text:"                                 # same value is passed but with input()
>>> k
['"', 't', 'e', 'x', 't', ':', '"']
>>> a=(10,20)                           # passing tuples
>>> k=list(a)
>>> k
[10, 20]
>>> k=list(input())
(10,20)
>>> k
['(', '1', '0', ',', '2', '0', ')']
>>> a={1:10,2:'a'}
>>> k=list(a)                           # passing dictionary - takes only key value
>>> k
[1, 2]
>>> k=list(input())
{1:10,2:'a'}
>>> k
['{', '1', ':', '1', '0', ',', '2', ':', "'", 'a', "'", '}']



#1.append():
#***********
    1. adds an item to the end of the list.
    2. The method takes a single argument(number, string, list,tuples,dictonaries etc.)
    3. The method doesn't return any value (returns None).

#Example
currencies = ['Dollar', 'Euro', 'Pound']
currencies.append('Yen')        # adding string
>>> currencies
['Dollar', 'Euro', 'Pound', 'Yen']
currencies.append(12)           # adding no.
>>> currencies
['Dollar', 'Euro', 'Pound', 'Yen', 12]
currencies.append([23,34,45])   # adding list
>>> currencies
['Dollar', 'Euro', 'Pound', 'Yen', 12, [23, 34, 45]]
currencies.append((23,34))      #adding tuples
>>> currencies
['Dollar', 'Euro', 'Pound', 'Yen', 12, [23, 34, 45], (23, 34)]
 currencies.append({1:23,2:34})      # adding Dictionaries
>>> currencies
['Dollar', 'Euro', 'Pound', 'Yen', 12, [23, 34, 45], (23, 34), {1: 23, 2: 34}]
q=currencies.append(80)             # method doesnot return any value
>>> q 
>>> list1=[12,23,34]
>>> q=currencies.append(list1.pop())    # function passesd as argument
>>> q
>>> currencies
['Dollar', 'Euro', 'Pound', 'Yen', 12, [23, 34, 45], (23, 34), {1: 23, 2: 34}, 80, 34]

# 2 . Extend
# ***********

    1. adds all the elements of an iterable (list, tuple, string etc.) to the end of the list.
    2. method takes an iterable such as list, tuple, string etc.
    3. method modifies the original list. It doesn't return any value.
#Example:
>>> a=[10,20]
>>> a.extend([30,40])           # passing list
>>> a
[10, 20, 30, 40]
>>> a.extend((50,60))           # passing tuples
>>> a
[10, 20, 30, 40, 50, 60]
>>> a.extend({1:100,2:200})     # passing Dictionaries
>>> a
[10, 20, 30, 40, 50, 60, 1, 2]
>>> a.extend('yen')             # passing string
>>> a
[10, 20, 30, 40, 50, 60, 1, 2, 'y', 'e', 'n']

#######Difference between append and extend##########################
#######************************************###########################
1.     Effect:      append() adds a single element to the end of the list while .
                    extend() can add multiple individual elements to the end of the list.

2.     Argument:    append() takes a single element as argument while .
                    extend() takes an iterable as argument (list, tuple, dictionaries, sets, strings).

3.                  append() adds all list,tuples,dictionaries into the list as same datatype
                but extend() adds all list,tuples,dictionaries(only keys) into the list as each individual element  

#3. insert()
#***********
     1. method inserts an element to the list at the specified index.
     2. The insert() method takes two parameters:
            index - the index where the element needs to be inserted
            element - this is the element to be inserted in the list
     3. method doesnt return anything; returns None. It only updates the current list.

#Example:
>>> a=[10,20]
>>> a.insert(0,'one')               # passing +ve index
>>> a
['one', 10, 20]
>>> a.insert(-1,'two')              # passing -ve index
>>> a
['one', 10, 'two', 20]
>>> a.insert(-1,(20,3))             # pasing tuples as element
>>> a
['one', 10, 'two', (20, 3), 20] 
>>> a.insert(-1,{1:20,30:900}       # passing dictionaries as element
	 )
>>> a
['one', 10, 'two', (20, 3), {1: 20, 30: 900}, 20]

#4. index()
#**********
    1. returns the index of the specified element in the list.
    2. The list index() method can take a maximum of three arguments:

            element - the element to be searched
            start (optional) - start searching from this index
            end (optional) - search the element up to this index
    3. The index() method returns the index of the given element in the list.
         If the element is not found, a ValueError exception is raised.
         Note: The index() method only returns the first occurrence of the matching element.
# Example:
>>> a=[10,20,30,10,20]
>>> a.index(10)             #adding element
0
>>> a.index(10,2)           # adding elt with start value
3
>>> a.index(10,2,4)         # adding elt with end value [ end is also included]
3
>>> a.index(10,2,3)         # Elt not present
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a.index(10,2,3)
ValueError: 10 is not in list
>>> a=['a','e',['a']]
>>> a.index('a')             
0
>>> a.index('a',1)          # Elt is not searched in nested list
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a.index('a',1)
ValueError: 'a' is not in list

#5. count()
#***********
    1. returns the number of times the specified element appears in the list.
    2. The count() method takes a single argument:
        element - the element to be counted
    3. returns the number of times element appears in the list.

# Example:
#*********
>>> a=[10,20,30,[10,20],40,50,[10,20]]  # It will not count if its nested
>>> a.count(10)
1
>>> a.count([10,20])
2

#6. sort()
##########
    1. sorts the items of a list in ascending or descending order.
    2. It has two optional parameters:
        reverse - If True, the sorted list is reversed (or sorted in Descending order)
    3. doesn't return any value. Rather, it changes the original list.

#Example::
a=[100,0,-1,20,9]           # can use negative no's
>>> a.sort()
>>> a
[-1, 0, 9, 20, 100]
>>> a=[100,100.5,100.0]     # can use float vlaues
>>> a.sort()
>>> a
[100, 100.0, 100.5]
#### We cannot use different datatype and also nested list###
>>> a=[30,200,10,0,'','a','k']
>>> a.sort()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
>>> a=[100,0,10,[10,0]]
>>> a.sort()
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'list' and 'int'

#7. sorted()
#############

    1.  sorts the elements of a given iterable in a specific order (ascending or descending) and returns it as a list.

    2.  sorted() can take a maximum of three parameters:

        iterable - A sequence (string, tuple, list) or collection (set, dictionary, frozen set) or any other iterator.
        reverse (Optional) - If True, the sorted list is reversed (or sorted in descending order). Defaults to False if not provided.
        key (Optional) - A function that serves as a key for the sort comparison. Defaults to None.

    3. returns a sorted list.

#Example:
#########
>>> a= [10,20,300,0,-1,10.5]
>>> sorted(a)
[-1, 0, 10, 10.5, 20, 300]
>>> a                               # sorted() will not change the original list
[10, 20, 300, 0, -1, 10.5]
############## same like sort() ,sorted() will not allow different datatype.############
>>> d=sorted(a)                     # function returns the valu e
>>> d
[-1, 0, 10, 10.5, 20, 300]

#8. remove()
############
    1.  removes the first matching element (which is passed as an argument) from the list.
    2.  takes single element as an argument and removes it from the list.
        If the element doesnt exist, it throws ValueError: list.remove(x): x not in list exception.
    3. doesnt return any value (returns None).

#Example:
>>> a=[10,20,30,10,0]
>>> a.remove(10)            # removes elt from list but if its contains duplicate elt it removes first occurences
>>> a
[20, 30, 10, 0]
>>> a=[10,20,[10]]
>>> a.remove(10)
>>> a
[20, [10]]
>>> a=[10,20,[10]]
>>> a.remove([10])       # if its specified in list it removes only the nested format
>>> a
[10, 20]
>>> a.remove(100)        # throws value error if elt not present
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    a.remove(100)
ValueError: list.remove(x): x not in list

# 9. clear:
###########
        1. removes all items from the list.
        2. The clear() method doesnt take any parameters.
        3. method only empties the given list. It doesnt return any value.

#example:
>>> list = [{1, 2}, ('a'), ['1.1', '2.2']]
>>> list.clear()
>>> list
[]

#10. pop()
##########
        1. removes the item at the given index from the list and returns the removed item.
        2. The pop() method takes a single argument (index).
                   The argument passed to the method is optional.
                   If not passed, the default index -1 is passed as an argument (index of the last item).
                   If the index passed to the method is not in range,
                            it throws IndexError: pop index out of range exception.
        3. returns the item present at the given index.

#Example:
>>> a=[1,2,3,'a','e',[10,20],(10,20)]
>>> a.pop()                             # takes no parameter
(10, 20)
>>> a
[1, 2, 3, 'a', 'e', [10, 20]]           
>>> a.pop(-3)                           # can specify negative index
'a'
>>> a
[1, 2, 3, 'e', [10, 20]]
>>> s=a.pop(2)                          # returns the value
>>> a
[1, 2, 'e', [10, 20]]
>>> s
3
>>> a=[]                                # It will give an IndexError saying pop from an empty list. 
>>> a.pop()
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    a.pop()
IndexError: pop from empty list

########Difference between del and pop and remove #########################3
    1. pop()and remove() is a function, and del is a keyword in Python.

    2. pop()    - removes the last element.
       remove() - removes the first occurrence of the specified element. 
       del      - remove single ,group of element using slicing or entire list.

    3. pop()    -It does not require a parameter; it is optional.
                -The value of the element is passed as the parameter.
                - It requires the index value, or else it deletes the whole list.

    4.          - It returns the value of the deleted element.
                - It does not return any value.
                - It does not return any value.

    5.          - It gives IndexError if the specified index is not found.
                - It gives ValueError if the specified value is not found.
                - It gives IndexError if the specified index is not found.

#del Example:
#############
>>> a=[10,20,30,[10,20],100,-1]
>>> del a[-1]
>>> a
[10, 20, 30, [10, 20], 100]
>>> del a[0:2]
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    a
NameError: name 'a' is not defined

#11.max()
#########
    1. returns the largest item in an iterable.
    2. argument - iterable - an iterable such as list, tuple,dictionary, etc.
    3. returns the largest element from an iterable.
#Example:
>>> a=[10,20,30,[10,20],'a','r']
>>> max(a)                          # cannot find the max value for different datatype
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    max(a)
TypeError: '>' not supported between instances of 'list' and 'int'
>>> a=[10,-1]
>>> max(a)
10
##########same for min() ##############

#12. sum()
##########
    1. adds the items of an iterable and returns the sum.
    2. takes two parameter
            iterable         - iterable (list, tuple, dict, etc). The items of the iterable should be numbers.
            start (optional) - this value is added to the sum of items of the iterable.
                               The default value of start is 0 (if omitted)
    3. returns the sum of start and items of the given iterable

#Example:
>>> a=[10,20,[10,20]]           # cannot pass different datatype
>>> sum(a)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    sum(a)
TypeError: unsupported operand type(s) for +: 'int' and 'list'
>>> a=[10,20,30]
>>> sum(a)
60
>>> a=sum(a)                    # it returns the value
>>> a
60
>>> a=[10,20,2.3]       
>>> k=sum(a,10)                 # adds elt to the sum
>>> k
42.3'''







