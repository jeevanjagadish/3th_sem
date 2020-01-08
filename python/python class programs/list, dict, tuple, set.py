Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s='asdfghjkl'
>>> s[0:3]
'asd'
>>> s[5:8]
'hjk'
>>> s[2:]
'dfghjkl'
>>> s = "jeev"+"mca"
>>> s
'jeevmca'
>>> s = "jeev"*"mca"
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    s = "jeev"*"mca"
TypeError: can't multiply sequence by non-int of type 'str'
>>> s = "jeev"
>>> s
'jeev'
>>> s = "jeev"*
SyntaxError: invalid syntax
>>> 
>>> s= "hekj"
>>> s*3
'hekjhekjhekj'
>>> s = "gegegae121"
>>> s s*4
SyntaxError: invalid syntax
>>> s = "kfsnk"
>>> s * 5
'kfsnkkfsnkkfsnkkfsnkkfsnk'
>>> 
>>> print("lknfev")
lknfev
>>> print["bwfkj"]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print["bwfkj"]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> print("nrfn"+"flf")
nrfnflf
>>> s =
SyntaxError: invalid syntax
>>> s = 'asasasas          '
>>> s
'asasasas          '
>>> s.strip()
'asasasas'
>>> s.len()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    s.len()
AttributeError: 'str' object has no attribute 'len'
>>> len(s)
18
>>> s
'asasasas          '
>>> s = s.strip()
>>> s
'asasasas'
>>> len(s)
8
>>> s =
SyntaxError: invalid syntax
>>> s = "egnkjeg"
>>> s = lower()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    s = lower()
NameError: name 'lower' is not defined
>>> s.lower()
'egnkjeg'
>>> s.upper()
'EGNKJEG'
>>> s
'egnkjeg'
>>> s = "wfnk"
>>> s = "wfnk"
>>> s = s.replace()
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    s = s.replace()
TypeError: replace() takes at least 2 arguments (0 given)
>>> s.replace()
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    s.replace()
TypeError: replace() takes at least 2 arguments (0 given)
>>> s=
SyntaxError: invalid syntax
>>> 
>>> s = 'ajasdhsdds'
>>> s.replace('j', 'u')
'auasdhsdds'
>>> s.replace('aja','cdc')
'cdcsdhsdds'
>>> s.replace('aja','cd')
'cdsdhsdds'
>>> s = "hello world, hello city"
>>> s.split("hello
	    
SyntaxError: EOL while scanning string literal
>>> s.split("hello")
	    
['', ' world, ', ' city']
>>> s = "mca is com app,mca"
	    
>>> s.split("mca")
	    
['', ' is com app,', '']
>>> s ="sfjlnfs"
	    
>>> s.capitalize()
	    
'Sfjlnfs'
>>> s = 'abcdabcdabcdabcdabcababababababasdfasdfab'
	    
>>> s.count('ab')
	    
12
>>> s = "jejbjkbwefkjbwf"
	    
>>> s.count
	    
<built-in method count of str object at 0x02984E80>
>>> 55555555555555555
	    
55555555555555555
>>> s.count("j")
	    
4
>>> s = "ljfklrf"
	    
>>> s.islower()
	    
True
>>> s = "fj1223"
	    
>>> s.islower()
	    
True
>>> s.isupper()
	    
False
>>> s = 'Jeevan is doing mca in pes uni. Jeevan is the topper of his class"
	    
SyntaxError: EOL while scanning string literal
>>> s = 'Jeevan is doing mca in pes uni. Jeevan is the topper of his class'
	    
>>> s.find("Jeevan")
	    
0
>>> s.find("mca")
	    
16
>>> tuple(asd)
	    
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    tuple(asd)
NameError: name 'asd' is not defined
>>> tuple('asdfasdf' , 'hello')
	    
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    tuple('asdfasdf' , 'hello')
TypeError: tuple expected at most 1 arguments, got 2
>>> tuple('asdf')
	    
('a', 's', 'd', 'f')
>>> s = tuple("jeevan")
	    
>>> len(s)
	    
6
>>> s
	    
('j', 'e', 'e', 'v', 'a', 'n')
>>> s.len()
	    
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    s.len()
AttributeError: 'tuple' object has no attribute 'len'
>>> tuple1= tuple('h','f')
	    
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    tuple1= tuple('h','f')
TypeError: tuple expected at most 1 arguments, got 2
>>> tuple1 = tuple(("g","r"))
	    
>>> tuple1
	    
('g', 'r')
>>> s = tuple("joker")
	    
>>> s
	    
('j', 'o', 'k', 'e', 'r')
>>> s[0:3]
	    
('j', 'o', 'k')
>>> s[0]='a'
	    
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    s[0]='a'
TypeError: 'tuple' object does not support item assignment
>>> set1 = set(("frj","fef"))
	    
>>> set1
	    
{'frj', 'fef'}
>>> set1.add("mca")
	    
>>> set1
	    
{'mca', 'frj', 'fef'}
>>> set1.remove("frj")
	    
>>> set1
	    
{'mca', 'fef'}
>>> len(set1)
	    
2
>>> tuple(("asd","ASd"))
	    
('asd', 'ASd')
>>> s = tuple(("asdf", "asdfasd"))
	    
>>> s[0:3]
	    
('asdf', 'asdfasd')
>>> s[0:1]
	    
('asdf',)
>>> l = list[2,3,4,41,1]
	    
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    l = list[2,3,4,41,1]
TypeError: 'type' object is not subscriptable
>>> l = list(1,3,4,512,3,4,23,12,412,412,3123,12,3,12,312,3,1233)
	    
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    l = list(1,3,4,512,3,4,23,12,412,412,3123,12,3,12,312,3,1233)
TypeError: list expected at most 1 arguments, got 17
>>> l = list((1,3,4,512,3,4,23,12,412,412,3123,12,3,12,312,3,1233))
	    
>>> l
	    
[1, 3, 4, 512, 3, 4, 23, 12, 412, 412, 3123, 12, 3, 12, 312, 3, 1233]
>>> l.append(123124124)
	    
>>> l
	    
[1, 3, 4, 512, 3, 4, 23, 12, 412, 412, 3123, 12, 3, 12, 312, 3, 1233, 123124124]
>>> l.remove(3))
SyntaxError: invalid syntax
>>> l.remove(3)
>>> l
[1, 4, 512, 3, 4, 23, 12, 412, 412, 3123, 12, 3, 12, 312, 3, 1233, 123124124]
>>> l = list(1,2,3,1,1,1,3,4,4,1,12,3,3)
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    l = list(1,2,3,1,1,1,3,4,4,1,12,3,3)
TypeError: list expected at most 1 arguments, got 13
>>> l = list((1,2,3,1,1,1,3,4,4,1,12,3,3))
>>> l
[1, 2, 3, 1, 1, 1, 3, 4, 4, 1, 12, 3, 3]
>>> l.remove(1)
>>> l
[2, 3, 1, 1, 1, 3, 4, 4, 1, 12, 3, 3]
>>> s = s((123,123,123,123))
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    s = s((123,123,123,123))
TypeError: 'tuple' object is not callable
>>> s = set((123,123,123,123))
>>> s.remove(123)
>>> s
set()
>>> s = set((123,123,153,133))
>>> s
{153, 123, 133}
>>> s.remove(123)
>>> s
{153, 133}
>>> l.clear
<built-in method clear of list object at 0x0112A7D8>
>>> l.clear()
>>> l
[]
>>> l = list((123,456,789))
>>> l2 = list((234,567,890))
>>> l
[123, 456, 789]
>>> l2
[234, 567, 890]
>>> l.extend(l2)
>>> l
[123, 456, 789, 234, 567, 890]
>>> l.copy()
[123, 456, 789, 234, 567, 890]
>>> l3 = l.copy()
>>> l3
[123, 456, 789, 234, 567, 890]
>>> l1 = list(("a","d"))
>>> l2 = list((1,2,3))
>>> l1.extend(l2)
>>> l1
['a', 'd', 1, 2, 3]
>>> l2
[1, 2, 3]
>>> l1.extend(list((22,34,33)))
>>> l1
['a', 'd', 1, 2, 3, 22, 34, 33]
>>> l1.extend(s)
>>> l1
['a', 'd', 1, 2, 3, 22, 34, 33, 153, 133]
>>> l1.extend(t)
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    l1.extend(t)
NameError: name 't' is not defined
>>> t = tuple(("asdf", "asdfasd"))
>>> l1.extend(t)
>>> l1
['a', 'd', 1, 2, 3, 22, 34, 33, 153, 133, 'asdf', 'asdfasd']
>>> l1.extend("asdf")
>>> l1
['a', 'd', 1, 2, 3, 22, 34, 33, 153, 133, 'asdf', 'asdfasd', 'a', 's', 'd', 'f']
>>> l = "addadadn"
>>> l.index("w")
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    l.index("w")
ValueError: substring not found
>>> l.index("4")
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    l.index("4")
ValueError: substring not found
>>> l = "addadadn"
>>> l.index("n")
7
>>> l.insert(8,"jfjagn")
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    l.insert(8,"jfjagn")
AttributeError: 'str' object has no attribute 'insert'
>>> l1
['a', 'd', 1, 2, 3, 22, 34, 33, 153, 133, 'asdf', 'asdfasd', 'a', 's', 'd', 'f']
>>> l1.index(133)
9
>>> l1.insert(10,"rtyui")
>>> l1
['a', 'd', 1, 2, 3, 22, 34, 33, 153, 133, 'rtyui', 'asdf', 'asdfasd', 'a', 's', 'd', 'f']
>>> l1.pop(3)
2
>>> l1.remove(10)
Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    l1.remove(10)
ValueError: list.remove(x): x not in list
>>> l1.remove(22)
>>> l1
['a', 'd', 1, 3, 34, 33, 153, 133, 'rtyui', 'asdf', 'asdfasd', 'a', 's', 'd', 'f']
>>> l1.reverse()
>>> l1
['f', 'd', 's', 'a', 'asdfasd', 'asdf', 'rtyui', 133, 153, 33, 34, 3, 1, 'd', 'a']
>>> l1.sort()
Traceback (most recent call last):
  File "<pyshell#163>", line 1, in <module>
    l1.sort()
TypeError: '<' not supported between instances of 'int' and 'str'
>>> l1 = list(5,7,2,1)
Traceback (most recent call last):
  File "<pyshell#164>", line 1, in <module>
    l1 = list(5,7,2,1)
TypeError: list expected at most 1 arguments, got 4
>>> l1 = list((1,3,4,2,7,0))
>>> l1.sort()
>>> l1
[0, 1, 2, 3, 4, 7]
>>> l1 = list(("a33","a22","b5"))
>>> l1.sort()
>>> l1
['a22', 'a33', 'b5']
>>> l1 = list(("a33","c22","b5"))
>>> l1.sort()
>>> l1
['a33', 'b5', 'c22']
>>> l1 = list(("1a3","c22","b5"))
>>> l1.sort()
>>> l1
['1a3', 'b5', 'c22']
>>> l1 = dict(("a"=5,"c22"=8,"b5"=9))
SyntaxError: invalid syntax
>>> l1 = dict(("a":5,"c22":8,"b5":9))
SyntaxError: invalid syntax
>>> l1 = dict("a":5,"c22":8,"b5":9)
SyntaxError: invalid syntax
>>> dict('a':123, 'b': 345)
SyntaxError: invalid syntax
>>> dict('a'=123, 'b'=345)
SyntaxError: keyword can't be an expression
>>> dict('a':123, 'b':345)
SyntaxError: invalid syntax
>>> d = dict('a':123, 'b':345)
SyntaxError: invalid syntax
>>> 
>>> d = dict('a':123,'b':345)
SyntaxError: invalid syntax
>>> d = dict('a'=123,'b'=345)
SyntaxError: keyword can't be an expression
>>> d = dict("a"=123,"b"=345)
SyntaxError: keyword can't be an expression
>>> 
>>> d = dict(("a"=123,"b"=345))
SyntaxError: invalid syntax
>>> d = dict(("a"="123","b"="345"))
SyntaxError: invalid syntax
>>> d = dict (("a"=123,"b"=345))
SyntaxError: invalid syntax
>>> d = dict (("jeev"=123,"eve"=345))
SyntaxError: invalid syntax
>>> d = dict ((jeev=123,eve=345))
SyntaxError: invalid syntax
>>> d = dict ((jeev:123,eve:45))
SyntaxError: invalid syntax
>>> d= dict(12:"asdf", 34:"qwer")
SyntaxError: invalid syntax
>>> d= dict(12="asdf", 34="qwer")
SyntaxError: keyword can't be an expression
>>> d = dict(a=1, b=123)
>>> d = dict(aASD=1, AS=123)
>>> D
Traceback (most recent call last):
  File "<pyshell#199>", line 1, in <module>
    D
NameError: name 'D' is not defined
>>> d
{'aASD': 1, 'AS': 123}
>>> d['asdf']=2134
>>> d
{'aASD': 1, 'AS': 123, 'asdf': 2134}
>>> hello = dict{'123':123}
SyntaxError: invalid syntax
>>> d
{'aASD': 1, 'AS': 123, 'asdf': 2134}
>>> 
[DEBUG ON]
>>> 
[DEBUG OFF]
>>> 
