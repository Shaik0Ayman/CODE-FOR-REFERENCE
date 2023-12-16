'''#1.capitalize()
#---------------
 1.This method returns the copy of the string with
      its first character capitalized and the rest of the letters lowercased.
    2. It will not modify the original string
    3. function will return the value .'''

#Example:Capitalize word
a = 'hello world!' 
b = a.capitalize()        
print('Original String:', a)  
print('New String:', b)

#capitalizing  a sentence
a = 'mumBai Is AWesome'
b = a.capitalize()
print('OriginaL String:', a)  
print('New String:', b)


#Example: Ignores Symbols & Numbers
address='#1 Harbor Side'.capitalize()
print(address)

#2. split()
#--------
'''The split() method splits the string from the specified separator and returns a list object with string elements.
The default separator is any whitespace character such as space, \t, \n, etc.
    2. It will not modify the original string
    3. function will return the value .'''

###Syntax: str.split(separator, maxsplit)

'''
1. separator: (optional) The delimiter string.
               The default separator is any whitespace character such as space, \t, \n, etc.
2. maxsplit: (optional) Defines the maximum number of splits that can be done.
                Thus, the list can contain at most maxsplit + 1 elements.
                The default maxsplit is -1 that means unlimited splits.
                '''
#Example: Split a String with Default Whitespace Chars
mystr = 'Hello World'
print(mystr.split())

print('Hello     World'.split())
print('Hello\tWorld'.split())
print('Hello\nWorld'.split())

#Example :Split using Separator
langs = 'C,Python,R,Java,SQL,Hadoop'
print(langs.split(','))

fruits = 'apples$banana$mango$fig$pear'
print(fruits.split('$'))


#Example: Split using Separator and maxsplit
langs = 'C,Python,R,Java,SQL,Hadoop'
print(langs.split(',', 3))

fruits = 'apples$banana$mango$fig$pear'
print(fruits.split('$', 2))

'''Note:The split() method will raise the ValueError if a separator is an empty string .'''


#3. replace()
#----------
'''The replace() method returns a copy of the string where all occurrences of a substring are replaced with another
substring.The number of times substrings should be replaced by another substring can also be specified.
    2. It will not modify the original string
    3. function will return the value .'''

###Syntax:str.replace(old,new,count)

#Example:replace()
mystr = 'Hello World!'
print(mystr.replace('Hello','Hi'))

mystr = 'apples, bananas, apples, apples, cherries'
print(mystr.replace('apples','lemons'))

#Example:Case sensitive replace- replace() method performs case-sensitive search.

mystr = 'Good Morning!'
print(mystr.replace('G','f')) # replace capital G

mystr = 'Good Morning!'
print(mystr.replace('good','food')) # can't find 'good'


mystr = 'Good Morning!'
print(mystr.replace('g','f')) # replace small g

#Example: replace() with Count
mystr = 'apples, bananas, apples, apples, cherries, apples'
print(mystr.replace('apples','lemons',2))

mystr = 'Python, Java, Python, C are programming languages'
print(mystr.replace('Python','SQL',1))

#Example: Replace Numbers or Symbols
mystr = '100'
print(mystr.replace('1','2'))

mystr = '#100'
print(mystr.replace('#','$'))

#Example: Replace Empty String
mystr = 'Hello World'
print(mystr.replace('World',''))

#4.find()
#--------
'''The find() method returns the index of the first occurence of a substring in the given string (case-sensitive).
If the substring is not found it returns -1.'''

###Syntax:str.find(substr, start, end)

#Example: find()
greet='Hello World!'
print("Index of 'H': ", greet.find('H'))
print("Index of 'h': ", greet.find('h')) # returns -1 as 'h' no found
print("Index of 'e': ", greet.find('e'))
print("Index of 'World': ", greet.find('World'))

#Example:The find() method returns an index of the first occurence only.
greet='Hello World'
print('Index of l: ', greet.find('l'))
print('Index of o: ', greet.find('o'))

mystr='tutorials is a free tutorials blog'
print('Index of tutorials: ', mystr.find('tutorials'))

#Example:The find() method performs case-sensitive search. It returns -1 if a substring is not found.
greet='Hello World'
print(greet.find('h'))  
print(greet.find('hello')) 
print(greet.find('Hi'))

#Example: find() with start and end
mystr='tutorialsteacher is a free tutorials blog'
print(mystr.find('tutorials', 10)) # search starts from 10th index
print(mystr.find('tutorials', 1, 26)) # searches between 1st and 26th index

#5. index()
#---------
'''The index() method returns the index of the first occurence of a substring in the given string.
It is same as the find() method except that if a substring is not found, then it raises an exception.
'''

### Syntax: str.index(substr,start,end)

#Example:
greet='Hello World!'
print('Index of H: ', greet.index('H'))
print('Index of e: ', greet.index('e'))
print('Index of l: ', greet.index('l'))
print('Index of World: ', greet.index('World'))

#Example:returns an index of the first occurance only.
greet='Hello World'
print('Index of l: ', greet.index('l'))
print('Index of o: ', greet.index('o'))

#Example:Case-sensitive index() Method
greet='Hello World'
#print(greet.index('h')) # throws error: substring not found 
#print(greet.index('hello')) # throws error

#Example:substring could not be found then it will throw an error.
mystr='TutorialsTeacher is a free online learning website'
#print(mystr.index('python'))

#Example: index() with start and end parameters
mystr='tutorialsteacher is a free tutorials website'
print(mystr.index('tutorials',10)) # search starts from 10th index
#print(mystr.index('tutorials',1, 26)) # throws error; searches between 1st and 26th index

#7.isaplha()
#-------------

'''True --- if all characters in the string are alphabets (can be both lowercase and uppercase).
   False --- if at least one character is not alphabet.'''
   
#Example 
name = "Monica"
print(name.isalpha())

# contains whitespace
name = "Monica Geller"
print(name.isalpha())

# contains number
name = "Mo3nicaGell22er"


#8.isalnum()
#--------------
'''The isalnum() method returns:

True - if all characters in the string are alphanumeric
False - if at least one character is not alphanumeric
'''

#Example:
# contains either numeric or alphabet
string1 = "M234onica"
print(string1.isalnum()) # True 

# contains whitespace
string2 = "M3onica Gell22er"
print(string2.isalnum()) # False

# contains non-alphanumeric character 
string3 = "@Monica!"
print(string3.isalnum()) # False 
print(name.isalpha())

#9. isdigit()
#--------------
'''The isdigit() returns:

True if all characters in the string are digits.
False if at least one character is not a digit.'''

#Example:
s = "28212"
print(s.isdigit())

# contains alphabets and spaces
s = "Mo3 nicaG el l22er"
print(s.isdigit())

#10. title()
#-------------

'''The first character of each word is capitalized (if the first character is a letter).
   method doesn't take any parameters.'''
#Example:
text = 'My favorite number is 25.'
print(text.title())

text = '234 k3l2 *43 fun'
print(text.title())

#11. count()
#-----------
'''count() method only requires a single parameter for execution. However, it also has two optional parameters:

substring - string whose count is to be found.
start (Optional) - starting index within the string where search starts.
end (Optional) - ending index within the string where search ends.
method returns the number of occurrences of the substring in the given string.'''

#Example:
string = "Python is awesome, isn't it?"
substring = "is"
count = string.count(substring)
print("The count is:", count)

#Example:
string = "Python is awesome, isn't it?"
substring = "i"
count = string.count(substring, 8, 25)
print("The count is:", count)

#12. lower()
#------------
''' method returns the lowercase string from the given string. It converts all uppercase characters to lowercase.
 If no uppercase characters exist, it returns the original string.
 method doesn't take any parameters.'''
#Example:
string = "THIS SHOULD BE LOWERCASE!"
print(string.lower())

string = "Th!s Sh0uLd B3 L0w3rCas3!"
print(string.lower())


#13. islower()
#--------------
'''The islower() method returns:

True if all alphabets that exist in the string are lowercase alphabets.
False if the string contains at least one uppercase alphabet.'''

#Example:

s = 'this is good'
print(s.islower())

s = 'th!s is a1so g00d'
print(s.islower())

s = 'this is Not good'
print(s.islower())

#14. upper()
#------------
'''upper() method returns the uppercase string from the given string. It converts all lowercase characters to uppercase.

If no lowercase characters exist, it returns the original string.'''
#Example::
string = "this should be uppercase!"
print(string.upper())
string = "Th!s Sh0uLd B3 uPp3rCas3!"
print(string.upper())

#15. isupper()
#---------------
'''The isupper() method returns:

True if all characters in a string are uppercase characters
False if any characters in a string are lowercase characters'''
# example 
string = "THIS IS GOOD!"
print(string.isupper());
string = "THIS IS ALSO G00D!"
print(string.isupper());
string = "THIS IS not GOOD!"
print(string.isupper());

#16.strip()
#------------
'''The original string with white spaces removed from the start and
end if the characters to be removed are not specified.

In case the string does not have any whitespaces at the start or end,
the string will be returned as it is and will match with the original string.

If the characters parameter is given, and if the characters are given matches,
the characters at the start or end of the string will be removed from the original string,
and the rest of the string will be returned.

Incase if the characters given does not match the start or the end in the original string,
the string will be returned as it is.'''

#Example:

str="    Welocme to python   "
print(str.strip())

str1 = "****Welcome to python!****"
after_strip = str1.strip("*")
print(after_strip)

str2 = "Welcome to python99!"
after_strip1 = str2.strip("99!")
print(after_strip1)
str3 = "Welcome to pythpn99!"
after_strip3 = str3.strip("to")
print(after_strip3)
