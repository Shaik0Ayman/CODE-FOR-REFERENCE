'''#dict()
#*******
1. creates a dictionary in Python.
2. It doesnt return any value

#Example:
#********
>>> a=dict()                                # Empty paranthesis --creates empty dict
>>> a
{}
>>> b=dict(x=5,y=10)                        # Create Dictionary Using keyword arguments only
>>> b
{'x': 5, 'y': 10}
>>>a=dict([['a',2],['b',3]])                # Create Dictionary Using Iterable-list of list
>>> a
>>> a=dict([(0,100),(1,200)])               # Create Dictionary Using Iterable -list inside tuples
>>> a  
{0: 100, 1: 200}
>>> a=dict(zip(['x', 'y', 'z'], [1, 2, 3])) #dict() with zip() --- used to specify key and values separately 
>>> a
{'x': 1, 'y': 2, 'z': 3}
>>> >>> a=dict(zip(['x', 'y'], [1, 2, 3]))  # Even if no of arguments doesnot match it just ignores the last value
>>> a
{'x': 1, 'y': 2}

#1.keys()
#********

        1. extracts the keys of the dictionary and returns the list of keys.
        2. doesnt take any parameters.
#Example:
#-------
>>>employee = {'name': 'Phill', 'age': 22, 'salary': 3500.0}
>>>dictionaryKeys = employee.keys()
>>>print(dictionaryKeys)
dict_keys(['name', 'age', 'salary'])

#2. values()
#***********
        1.  returns a  list of all the values in the dictionary.
        2.  doesnt take any parameters.

#Example:
#--------
>>>marks = {'Physics':67, 'Maths':87}
>>>print(marks.values())
dict_values([67, 87])

#3. items()
#**********
        1. returns a list of dictionarys (key, value) tuple pairs.
        2. doesnt take any parameters.
#Example:
#--------
>>>sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
>>>print(sales.items())
dict_items([('apple', 2), ('orange', 3), ('grapes', 4)])

#4. get()
#*********
        1. returns the value for the specified key if the key is in the dictionary.
        2. takes maximum of two parameters:
                key - key to be searched in the dictionary
                value (optional) - Value to be returned if the key is not found. The default value is No ne.__bool__
        3. It returns
                 the value for the specified key if key is in the dictionary.
                 None if the key is not found and value is not specified.
                 value if the key is not found and value is specified.
#Example:
#--------
>>> person = {'name': 'Phill', 'age': 22}
>>> print('Name: ', person.get('name'))                 # with key without value
Name:  Phill
>>> print('Salary: ', person.get('salary', 0.0))        #key not present so it returns value provided
Salary:  0.0
>>> >>> print('Salary: ', person.get('salary'))         #key not present returns None
Salary:  None

#Different between get()  Vs dict[key] to Access Elements#
#----------------------------------------------------------#
    1. get() method returns a default value if the key is missing.
    2. However, if the key is not found when you use dict[key], KeyError exception is raised.

>>>d={1:100,2:200}
>>> d.get(0)
>>> print(d.get(0))
None
>>> d[0]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    d[0]
KeyError: 0



#5. update:
#**********
        1. The update() method adds element(s) to the dictionary if the key is not in the dictionary.
           If the key is in the dictionary, it updates the key with the new value.
        2. takes either a dictionary or an iterable object of key/value pairs (generally tuples).
        3. It doesnt return any value

#Example:
#--------
d = {1: "one", 2: "three"}
d1 = {2: "two"}
d.update(d1)                                 #updates the value of key 2
print(d)
{1: 'one', 2: 'two'}

d1 = {3: "three"}
d.update(d1)                                # adds element with key 3
print(d)
{1: 'one', 2: 'two', 3: 'three'}

dictionary = {'x': 2}
dictionary.update([('y', 3), ('z', 0)])     # we have passed a list of tuples tuple as argument
print(dictionary)
{'x': 2, 'y': 3, 'z': 0}


d={1:100}
>>> d.update([[0,100,2]])                   # if more than 2 arg is passed it raises an error            
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    d.update([[0,100,2]])
ValueError: dictionary update sequence element #0 has length 3; 2 is required


#6.clear()
#*********
        1. removes all items from the dictionary.
        2. No argument No return value

#Example:
#--------
numbers = {1: "one", 2: "two"}
numbers.clear()
print(numbers)

# Output: {}
        
#7.copy()
#********
            1. returns a copy (shallow copy) of the dictionary.
            2. method doesn't take any arguments.
            3. returns a shallow copy of the dictionary. It doesn't modify the original dictionary.


#Example
original = {1:'one', 2:'two'}
new = original.copy()
print('Orignal: ', original)
print('New: ', new)
Orignal:  {1: 'one', 2: 'two'}
New:  {1: 'one', 2: 'two'}

#copy() Method Vs = Operator
#----------------------------
        1. copy() is used as a copy of the references from the original dictionary.
        2. = operator is used, a new reference to the original dictionary is created.

#Example:
#--------
original = {1:'one', 2:'two'}
new = original
new.clear()                     #Using = Operator to Copy Dictionaries
print('new: ', new)
print('original: ', original)

new:  {}
original:  {}

original = {1:'one', 2:'two'}
new = original.copy()         # Using copy() to Copy Dictionaries
new.clear()
print('new: ', new)
print('original: ', original)

new:  {}
original:  {1: 'one', 2: 'two'}

#8. pop()
#********
        1. returns an element from a dictionary having the given key.
        2. takes two parameters:
                key - key which is to be searched for removal
                default - value which is to be returned when the key is not in the dictionary
        3. If key is found - removed/popped element from the dictionary
           If key is not found - value specified as the second argument (default)
           If key is not found and default argument is not specified - KeyError exception is raised
#Example:
#--------
>>> d={1:100,2:200,3:3000}
>>> d.pop(1)                # key is found -elt is removed
100
>>> d.pop(0)                # key is not found - displays error
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    d.pop(0)                
KeyError: 0
>>> d.pop(0,200)            # key is not found but value is specified so its returned
200

#9. popitem()
#************

        1. removes and returns the last element (key, value) pair inserted into the dictionary.
        2. doesnt take any parameters.
        3. Returns the latest inserted element (key,value) pair from the dictionary.
#Example:
>>> d={1:100,2:200,3:3000}
>>> d.popitem()                 # removes last item
(3, 3000)
>>> d
{1: 100, 2: 200}
>>> d={}
>>> d.popitem()                 # when dictionary is empty it raises key error
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    d.popitem()
KeyError: 'popitem(): dictionary is empty

#10.del()
#********
    1. Deletes the item with the given key or deletes the whole dictionary
    2. 
#Example:
#-------
>>> dict1 = {'Mohan':95,'Ram':89,
'Suhel':92, 'Sangeeta':85}
>>> del dict1['Ram']
>>> dict1
{'Mohan':95,'Suhel':92, 'Sangeeta': 85}

>>> del dict1
>>> dict1
NameError: name 'dict1' is not defined

#11.fromkeys()
#**************

        1. creates a dictionary from the given sequence of keys and values.
        2. take two parameters
                -alphabets - keys that can be any iterables like string, set, list, etc.
                -numbers (Optional) - are the values that can be of any type or any iterables like string,list, etc.
        3. returns sequence of keys and values,If the value of the dictionary is not provided, None is assigned to the keys.
        
#Example:
>>> x="abc"
>>> d=dict.fromkeys(x)                  #creating dictionary from sequence of keys
>>> d
{'a': None, 'b': None, 'c': None}
>>> x=[10,20,30]
>>> d=dict.fromkeys(x,1000)             # creating dictionary from keys and values 
>>> d
{10: 1000, 20: 1000, 30: 1000}
>>> x=(10,20,30)
>>> y=[10,20,30]
>>> d=dict.fromkeys(x,y)                # creating dictionary from keys and values
>>> d
{10: [10, 20, 30], 20: [10, 20, 30], 30: [10, 20, 30]}
>>> y.append(40)                        # when we append list dictionary also gets modified
>>> y.append(50)
>>> d
{10: [10, 20, 30, 40, 50], 20: [10, 20, 30, 40, 50], 30: [10, 20, 30, 40, 50]}

#12.setdeafult()
#---------------
        1.  returns the value of a key (if the key is in dictionary).
            If not, it inserts key with a value to the dictionary.
        2. takes a maximum of two parameters:
                key - the key to be searched in the dictionary
                default_value (optional) - key with a value default_value is inserted to the dictionary
                 if the key is not in the dictionary.
                If not provided, the default_value will be None.
#Example:
#--------
>>> person = {'name': 'Phill', 'age': 22}
>>> age = person.setdefault('age')                  # age is key so it returns associated value
>>> age
22
>>> print(person.setdefault('class'))               # class in not key so it is addded as one elt ,default value is None
None
>>> person
{'name': 'Phill', 'age': 22, 'class': None}
>>> print(person.setdefault('section','A'))         # section is not key and value is provided ,
A
>>> person
{'name': 'Phill', 'age': 22, 'class': None, 'section': 'A'}


#13.max()
#*********
        1. max() returns the largest key
#Example:
#--------
square = {2: 4, -3: 9, -1: 1, -2: 4}
key1 = max(square)
print("The largest key:", key1)
The largest key: 2

>>> d={'anu':490 ,'priya':478,'Zahir':490}     # string is passed as a key
>>> max(d)
'priya'

>>> d={1:100,'a':20,(10,20):90}                 # In max() ,we cannot pass different keys.will raise error
>>> max(d)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    max(d)
TypeError: '>' not supported between instances of 'str' and 'int'
                
#######Same like min()##############

#14.sorted()
#***********
        1. To arrange in asc/des order
        2. return the value

#Example:
#---------
>>> py_set = {'e', 'a', 'u', 'o', 'i'}
>>> print(sorted(py_set))               #Its sorted in ascending order
['a', 'e', 'i', 'o', 'u']
>>> py_set                              # but it doesnt affect original string
{'o', 'a', 'u', 'i', 'e'}
>>> b=sorted(py_set,reverse=True)       # To sort in descending order
>>> b
['u', 'o', 'i', 'e', 'a']
>>> py_set
{'o', 'a', 'u', 'i', 'e'}
'''