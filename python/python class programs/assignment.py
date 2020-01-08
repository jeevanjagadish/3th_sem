1.check if two strings are anagrams of each other

>>> x= "jeev"
>>> y="jeev"
>>> x == y
True
>>> sorted(x)==sorted(y)
True




3. Read  a number n and comput n+nn+nnn

>>> n = int(input("enter a no"))
enter a no5
>>> temp = str(n)
>>> t1=temp+temp
>>> t2=temp+temp+temp
>>> comp=n+int(t1)+int(t2)
>>> print("the value is",comp)
the value is 615

4. form a new string where the first character and the last charcter are exchanged

>>> str=input("enter the string")
enter the stringMCA
>>> x = str[0]
>>> y = str[-1]
>>> newstr=y+str[1:-1]+x
>>> print(newstr)
ACM

5. remove spaces from a string

>>> string = "Master of Computer Application"
>>> string = string.replace(' ','')
>>> print(string)
MasterofComputerApplication

6.perform union,intersection,set difference,symmetric

>>> A = {1,2,3,4,5}
>>> B = {4,5,6,7,8}
>>> print('Union')
Union
>>> print(A | B)
{1, 2, 3, 4, 5, 6, 7, 8}
>>> print('intersection')
intersection
>>> print(A & B)
{4, 5}
>>> print('set difference')
set difference
>>> print(A-B)
{1, 2, 3}
>>> print('symmetric')
symmetric
>>> print(A^B)
{1, 2, 3, 6, 7, 8}

7. area and circumference of a circle
 
>>> print('area and circumference of the circle')
area and circumference of the circle
>>> ans = int(input("enter the radis"))
enter the radis 8
>>> ans1 = 3.14*r*r
>>> print(ans1)
200.96
>>> ans2 = 2*3.14*r
>>> print(ans2)
50.24
>>> 

8. comma separated numbers and generate a list and tuple.

>>> a = input("enter th no")
enter the no 7 7 8 5 
>>> x = [a]
>>> y = (a)
>>> print("here is the list"+str(x))
here is the list[' 7 7 8 5 ']
>>> print("here is the tuple"+str(y))
here is the tuple (7 7 8 5) 

9.filename and extension.

>>> filename = input("input fle name")
input fle name jeeva.pdf
>>> f_exten3 =  filename.split(".")
>>> print("file is" + repr(f_exten3[-1]))
file is'pdf'


10.diplay color in the odd numers.

>>> color_list = ["red","green","white","black","blue","yellow"]
>>> print(color_list[1],color_list[3],color_list[5])
green black yellow
>>>

11.area of the triangle

 B = int(input("enter the base") )
enter the base 5
>>> H = int(input("enter the height"))
enter the height 6
>>> area = B*H/2
>>> print("area",area)
area 15.0
>>> 


12.simple interest

 P = float(input("enter the principle amt"))
enter the principle amt 5.5
>>> t = int(input("enter the time"))
enter the time 3
>>> r = float(input("enter the rate"))
enter the rate 8
>>> si = (P*t*r)/100
>>> print("the simple interest is",si)
the simple interest is 1.32
>>> 

13.calculate BMI.

w = int(input("enter the weight"))
enter the weight 80
>>> z = float(input("enter the height"))
enter the height 5.11
>>> bmi = (w/(z*z))
>>> print("value is",bmi)
value is 3.0637137572236623
>>> 

14. sorting

>>> x = int(input("enter the 1st no"))
enter the 1st no 8
>>> y = int(input("enter the 2ns no"))
enter the 2ns no 5
>>> z = int(input("enter the 3rd no"))
enter the 3rd no 2
>>> a1 = min(x,y,z)
>>> a2 = max(x,y,z)
>>> a3 = (x+y+z) - a1 - a2
>>> print("sorted numbers are",a1,a2,a3)
sorted numbers are 2 5 8
>>> 

15.conctenate two tuples

>>> a = (1,2,3)
>>> b = (4,5,6)
>>> a+b
(1, 2, 3, 4, 5, 6)
>>> 

16. create a tuple of two tuples.
 
>>> j1 = (5,6,7,8)
>>> j2 = ('j','e','e','v')
>>> print(j1)
(5, 6, 7, 8)
>>> print(j2)
('j', 'e', 'e', 'v')
>>> j3 = ("A",j1,'B',j2)
>>> print(j3)
('A', (5, 6, 7, 8), 'B', ('j', 'e', 'e', 'v'))
>>> 

17.swap first two character of each string

>>> str1 = "ABC"
>>> str2 ="XYZ"
>>> C = str2[0:2]+str1[2:]
>>> D = str1[0:2]+str2[2:]
>>> print(C+" "+D)
XYC ABZ


18.swap second and last character in a sring

>>> str=input("enter the string")
enter the stringMCA
>>> x = str[0]
>>> y = str[-1]
>>> newstr=y+str[1:-1]+x
>>> print(newstr)
MAC

19.arrang the sorted form.

>>> words = "green-red-yellow-black"
>>> print("-".join(sorted(words.split("-"))))
black-green-red-yellow
>>> 