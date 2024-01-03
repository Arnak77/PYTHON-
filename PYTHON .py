#!/usr/bin/env python
# coding: utf-8

# # PYTHON PROGRAMMING LANGUAGE
# 

# In[30]:


1 + 1 # ADDITION


# In[31]:


2-1


# In[32]:


3*4


# In[33]:


8 / 4 # Division


# In[34]:


8 / 5 #float division


# In[35]:


8/4 ## float division 


# In[36]:


8 // 4 #integer division


# In[37]:


8 + 9 - 7


# In[38]:


8 + 8 - #syntax error:


# In[39]:


5 + 5 * 5


# In[40]:


(5 + 5) * 5 # BODMAS (Bracket || Oders || Divide || Multiply || Add || Substact)


# In[41]:


2 * 2 * 2 * 2 * 2 # exponentaion


# In[42]:


2 * 5


# In[43]:


2 ** 5


# In[44]:


15 / 3


# In[45]:


10 // 3 


# In[46]:


15 % 2 # Modulus 


# In[47]:


10 % 2 


# In[48]:


15 %% 2


# In[49]:


3 + 'nit'


# In[50]:


a,b,c,d,e = 15, 7.8, 'nit', 8+9j, True
print(a)
print(b)
print(c)
print(d)
print(e)


# In[51]:


print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))


# In[52]:


type(c)


#  <h3>So far we code with numbers(integer)
#      Lets work with string<h3>

# In[53]:


'Naresh IT'


# In[54]:


print('Max it')


# In[55]:


"max it technology"


# In[56]:


s1 = 'max it technology'
s1


# In[57]:


a = 2
b = 3
a + b


# In[58]:


c = a + b
c


# In[59]:


a = 3
b = 'hi'
type(b)


# In[60]:


print('max it's"Technology"') #\ has some special meaning to ignore the error


# In[61]:


print('max it\'s"Technology"') #\ has some special meaning to ignore the error


# In[62]:


print('max it',  'Technology')


# In[63]:


print("max it',  'Technology")


# In[64]:


# print the nit 2 times 
'nit' + ' nit'


# In[65]:


'nit'  ' nit'


# In[66]:


#5 time print
10 *'nit'


# In[67]:


10 *' nit' # soace between words


# In[68]:


print('c:\nit') #\n -- new line


# In[69]:


print(r'c:\nit') #raw string


# # variable || identifier || object

# In[70]:


2


# In[71]:


x = 2 #x is variable/identifier/objec, 2 is the value
x


# In[72]:


x + 3


# In[73]:


y = 3
y


# In[74]:


x + y


# In[75]:


x = 9
x


# In[76]:


x + y


# In[77]:


x + 10


# In[78]:


_ + y # _ understand the previous result of the 


# In[79]:


_ + y


# In[80]:


_ + y


# In[81]:


_ + y


# In[82]:


y


# In[83]:


_ + y


# In[84]:


_ + y


# In[85]:


_ + y


# In[86]:


# string variable 
name = 'mit'


# In[87]:


name


# In[88]:


name + 'technology'


# In[89]:


name + ' technology'


# In[90]:


name 'technology'


# In[91]:


name


# In[92]:


len(name)


# In[93]:


name[0] #python index begins with 0


# In[94]:


name[5]


# In[95]:


name[7]


# In[96]:


name[-1]


# In[97]:


name[-2]


# In[98]:


name[-6]


# # slicing

# In[99]:


name


# In[100]:


name[0:1] #to print 2 character  


# In[101]:


name[0:2]


# In[102]:


name[1:4]


# In[103]:


name[1:]


# In[104]:


name[:4]


# In[105]:


name[3:9]


# In[106]:


name1 = 'fine'
name1


# In[107]:


name1[0:1]


# In[108]:


name1[0:1] = 'd' # i want to change 1st character of naresh (n) - t


# In[109]:


name1[0] ='d' #strings in python are immutable


# In[110]:


name1


# In[111]:


name1[1:]


# In[112]:


'd' + name1[1:] #i want to change fine to dine


# In[113]:


len(name1) #python inbuild function 


# # List

# In[114]:


# LIST LIST LIST
nums = [10,20,30]
nums


# In[115]:


nums[0]


# In[116]:


nums[-1]


# In[117]:


nums[1:]


# In[118]:


nums[:1]


# In[119]:


num1 = ['hi', 'hallo']


# In[120]:


num1


# In[121]:


num2 = ['hi', 8.9, 34] # we can assign multiple variable 
num2


# In[122]:


# can we have 2 list together
num3 = [nums, num1]


# In[123]:


num3


# In[124]:


num4 = [nums, num1, num2]


# In[125]:


num4


# In[126]:


nums


# In[127]:


nums.append(45)


# In[128]:


nums


# In[129]:


nums.remove(45)


# In[130]:


nums


# In[131]:


nums.pop(1)


# In[132]:


nums


# In[133]:


nums.pop() #if you dont assign the index element then it will consider by default last index


# In[134]:


num1


# In[135]:


num1.insert(0,1)


# In[136]:


num1


# In[137]:


#if you want to delate multiple value 
num2


# In[138]:


del num2[2:]


# In[139]:


num2


# In[140]:


# if you need to add multiple values 
num2.extend([29,15,20])


# In[141]:


num2


# In[142]:


num2


# In[143]:


num3


# In[144]:


num3.extend(['a', 5, 6.7])


# In[145]:


num3


# In[146]:


num3


# In[147]:


nums


# In[148]:


min(nums) #inbuild function 


# In[149]:


max(nums) #inbuild function 


# In[150]:


num1 


# In[151]:


min(num1)


# In[152]:


sum(nums) #inbuild function


# In[153]:


nums.sort() #sort method


# In[154]:


nums


# # Tuple

# In[155]:


# TUPLE TUPLE TUPLE
tup = (15,25,35)
tup


# In[156]:


tup[0]


# In[157]:


tup[0] = 10


# ##### as we are unable to change any value or parameter in tuple so iteration very faster in tuple compare to list

# # SET

# In[158]:


# SET SET SET 
S = {}


# In[159]:


s1 = {21,6,34,58,5} 


# In[160]:


s1


# In[161]:


s3= {50,35,53,'nit', 53}


# In[162]:


s3.


# In[163]:


s1[1] #as we dont have proper sequencing thats why indexing not subscriptable


# # DICTIONARY

# In[164]:


# DICTIONARY DICTIONARY DICTIONARY
data = {1:'apple', 2:'banana',4:'orange'}
data


# In[165]:


data[4]


# In[166]:


data[3]


# In[167]:


data.get(2)


# In[168]:


data.get(3)


# In[169]:


print(data.get(3))


# In[170]:


data.get(1,'Not Fount')


# In[171]:


data.get(3,'Not Found')


# In[172]:


data[5] = 'five'


# In[173]:


data


# In[174]:


data


# In[175]:


del data [5]


# In[176]:


data


# In[177]:


data


# In[178]:


#list in the dictionary
prog = {'python':['vscode', 'pycharm'], 'machine learning' : 'sklearn', 'datascience':['jupyter','spyder'] }


# In[179]:


prog


# In[180]:


prog


# In[181]:


prog['python']


# In[182]:


prog['machine learning']


# In[183]:


prog['datascience']


# # introduce to ID()

# In[184]:


# variable address
num = 5
id(num)


# In[185]:


print(id(num))


# In[186]:


name = 'nit'
id(name) #Address will be different for both


# In[187]:


a = 10
id(a)


# In[188]:


b = a #thats why python is more memory efficient 


# In[189]:


id(b)


# In[190]:


id(10)


# In[191]:


k = 10 
id(k)


# In[192]:


a = 20  # as we change the value of a then address will change
id(a)


# In[193]:


id(b)


# what ever the variale we assigned the memory and we not assigned anywhere then we can use as garbage collection.|| VARIABLE - we can change the values || CONSTANT - we cannot change the value -can we make VARIABLE as a CONSTANT (note - in python you cannot make variable as constant)

# In[194]:


PI = 3.14  #in math this is alway constant but python we can chang
PI


# In[195]:


PI = 3.15
PI


# In[196]:


type(PI)


# In[197]:


PI


# # DATA TYPES & DATA STRUCTURES-->

# DATA TYPES & DATA STRUCTURES-->
# 1- NUMERIC || 2-LIST || 3-TUPLE || 4-SET || 5-STRING || 6-RANGE || 7-DICTIONAR

# 1- NUMERIC :- INT || FLOAT || COMPLEX || BOOL

# In[198]:


w = 2.5
type(w)


# In[199]:


(a)


# In[200]:


w2 = 2 + 3j #so hear j is represent as root of -1
type(w2)


# In[201]:


#convert flot to integer 
a = 5.6
b = int(a)


# In[202]:


b


# In[203]:


type(b)


# In[204]:


type(a)


# In[205]:


k = float(b)


# In[206]:


k


# In[207]:


print(a)
print(b)
print(k)


# In[208]:


k1 = complex(b,k)


# In[209]:


print(k1)
type(k1)


# In[210]:


b < k


# In[211]:


condition = b<k
condition


# In[212]:


type(condition)


# In[213]:


int(True)


# In[214]:


int(False)


# In[215]:


s = {1,2,3,4}
s


# In[216]:


type(s)


# In[217]:


s1 = {1,2,3,4,4,3,11} #duplicates are not allowed
s1


# In[218]:


t = (10,20,30)
t


# In[219]:


type(t)


# In[220]:


str = 'nit' #we dont have character in python 
type(str)


# # range()

# In[221]:


r = range(0,10)
r


# In[222]:


type(r)


# In[223]:


type(r)
# if you want to print the range 
list(range(0,10))


# In[224]:


#if you want to print even number
even_number = list(range(2,10,2))
even_number 


# In[225]:


d= {1:'one', 2:'two', 3:'three'}
d    


# In[226]:


type(d)


# In[227]:


# print the keys 
d.keys()


# In[228]:


d.values()


# In[229]:


# how to get particular value 
d[2]


# In[230]:


# other way to get value as
d.get(2)


# # operator

# # operator
# 1- ARITHMETIC OPERATOR ( + , -, *, /, %, %%, **, ^ 2- ASSIGNMEN OPERATOR (=) 3- RELATIONAL OPERATOR 4- LOGICAOPERATOR 5- UNARY OPERATOR 

# # Arithmetic operator

# In[231]:


x1, y1 = 10,  5 #x1 ^ y1


# In[232]:


x1  + y1 


# In[233]:


x1 - y1


# In[234]:


x1 * y1


# In[235]:


x1 / y1


# In[236]:


x1 // y1


# In[237]:


x1 % y1 


# In[238]:


x1 ** y1


# In[239]:


x2 =3
y2 = 3
x2 ** y2


# # Assignment operator

# In[240]:


x = 2


# In[241]:


x = x + 2 # if you want to increment by 2 


# In[242]:


x


# In[243]:


x += 2
x


# In[244]:


x += 2
x


# In[245]:


x *= 2


# In[246]:


x


# In[247]:


x -= 2


# In[248]:


x


# In[249]:


x /= 2


# In[250]:


x


# In[251]:


a, b = 5,6 # you can assigned variable in one line as well


# In[252]:


a


# In[253]:


b


# # unary operator

# unary means 1 || binary means 2
# Here we are applying unary minus operator(-) on the operand n; the value of m becomes -7, which indicates it as a negative value.

# In[254]:


n = 7 #negattion
n


# In[255]:


m = -(n)
m


# In[256]:


n


# In[257]:


-n


# # Relational operator

# In[258]:


a = 5
b = 6


# In[259]:


a<b


# In[260]:


a>b


# In[261]:


# a = b # we cannot use = operatro that means it is assigning 


# In[262]:


a == b


# In[263]:


a != b


# In[264]:


# hear if i change b = 6
b = 5


# In[265]:


a == b


# In[266]:


b


# In[267]:


a >= b


# In[268]:


a <= b


# In[269]:


a < b


# In[270]:


a>b


# In[271]:


b = 7


# In[272]:


a != b


# # LOGICAL OPERATOR

# LOGICAL OPERATOR
# logical operator you need to understand about true & false table image.png
# 3 importand part of logical operator is --> AND, OR, NOT

# In[273]:


a = 5
b = 4


# In[274]:


a < 8 and b < 5 #refer to the truth table 


# In[275]:


a < 8 and b < 2


# In[276]:


a < 8 or b < 2


# In[277]:


a>8 or b<2


# In[278]:


not x  # you can reverse the operation


# In[279]:


x = not x
x


# In[280]:


x


# In[281]:


not x


# # Number system coverstion (bit-binary digit)

# In the programing we are using binary system, octal system, decimal system & hexadecimal system

# In[282]:


bin(25)


# In[283]:


0b11001


# In[284]:


int(0b11001)


# In[285]:


bin(7)


# In[286]:


oct(25)


# In[287]:


0o31


# In[288]:


bin(7)


# In[289]:


oct(25)


# In[290]:


0o31


# In[291]:


int(0o31)


# In[292]:


hex(25)


# In[293]:


hex(16)


# In[294]:


0xb


# # swap 2-variable in python

# (a,b = 5,6) After swap we should get ==> (a, b = 6,5 )

# In[295]:


a = 5
b = 6


# In[296]:


a = b
b = a


# In[297]:


print(a)
print(b)


# In[298]:


# in above scenario we lost the value 5 
a1 = 7
b1 = 8


# In[299]:


temp = a1 
a1 = b1
b1 = temp


# In[300]:


print(a1)
print(b1)


# # method 2nd

# In[301]:


a2 = 5
b2 = 6


# In[302]:


#swap variable formulas without using 3rd formula
a2 = a2 + b2 # 5+6 = 11
b2 = a2 - b2 # 11-6 = 5
a2 = a2 - b2 # 11-5 = 6 


# In[303]:


print(a2)
print(b2)


# # method 3rd

# In[304]:


print(0b101) # 101 is 3 bit 
print(0b110) # 110 also 3bit 


# In[305]:


print(0b110)
print(0b101)


# In[306]:


#but when we use a2 + b2 then we get 11 that means we will get 4 bit which is 1 bit extra 
print(bin(11))
print(0b1011)


# # method 4

# In[307]:


print(a2)
print(b2)


# In[308]:


#there is other way to work using swap variable also which is XOR because it will not waste extra bit 
a2 = a2 ^ b2
b2 = a2 ^ b2
a2 = a2 ^ b2


# In[309]:


print(a2)
print(b2)


# # method 5

# In[310]:


a2, b2


# In[311]:


a2 ,b2 = b2, a2 # how it work is b2 6 a2 is 5 first it goes into stack & then it reverse the 2 vlaues


# In[312]:


print(a2)
print(b2)


# # BITWISE OPERATOR

# WE HAVE 6 OPERATORS COMPLEMENT ( ~ ) || AND ( & ) || OR ( | ) || XOR ( ^ ) || LEFT SHIFT ( << ) || RIGHT SHIFT

# In[313]:


print(bin(12))
print(bin(13))


# In[314]:


0b1101


# In[315]:


0b1100


# In[316]:


# COMPLEMENT (~) (TILDE  OR TILD)
~12 # why we get -13 . first we understand what is complment means (reversr of binary format)


# In[317]:


~46


# In[318]:


~54


# In[319]:


~-6


# In[320]:


~-1


# # bit wise and operator

# AND - LOGICAL OPERATOR ||| & - BITWISE AND OPERATOR
# (we know that 1 & 1 is 1) 12 - 00001100 13 - 00001101 when we are add both then then outut we will get as 12

# In[321]:


12 & 13


# In[322]:


12 | 13


# In[323]:


1 & 0


# In[324]:


1 | 0


# In[325]:


35 & 40 


# In[326]:


35 | 40


# In[327]:


# in XOR if the both number are different then we will get 1 or else we will get 0

12 ^ 13


# In[328]:


25^30


# In[329]:


# BIT WISE LEFT SHIFT OPERATOR 
# in left shift what we need to to we need shift in left hand side & need to shift 2 bits
#bit wise left operator bydefault you will take 2 zeros ( )
#10 binary operator is 1010 | also i can say 1010


# In[330]:


10<<2


# In[331]:


10<<3


# In[332]:


bin(20)


# In[333]:


0b101000000


# In[334]:


20<<4 #can we do this


# # BITWISE RIGHTSHIFT OPERATOR

# left side we are gaining the bits
# right side we are lossing bits

# In[335]:


bin(10)


# In[336]:


10>>2


# In[337]:


10>>3


# In[338]:


bin(20)


# In[339]:


20>>4


# In[340]:


x=sqrt(25) #sqrt is inbuild function


# In[341]:


import math # math is module


# In[342]:


x = math.sqrt(25)
x


# In[343]:


x1 = math.sqrt(15)
x1


# In[344]:


print(math.floor(3.87)) #floor - minimum or least value 


# In[345]:


print(math.ceil(3.87)) #ceil - maximum or highest value


# # import math function

# In[346]:


print(math.pow(3,2))


# In[347]:


print(math.pi) #these are constant


# In[348]:


print(math.e) # e - epsilon values


# In[349]:


m.sqrt(25) 


# In[350]:


import math as m # we need to use concept aliseing, instead of math we are using as m
m.sqrt(10) #if you are lazy to type then you can use m or else you can use math 


# In[351]:


from math import sqrt,pow # math has many function if you want to import specific function then use import
print(pow(2,3))
print(math.sqrt(10))


# In[352]:


round(pow(2,3))


# # user input function in python || command line input

# how to get input from user

# In[353]:


x = input()
y = input()
z = x + y
print(z) # console is waiting for user to enter input 
# also if you work in idle


# In[354]:


type(x)


# In[355]:


x1 = input('Enter the 1st number') #whenevery you works in input function it always give you string 
y1 = input('Enter the 2nd number') # it wont understand as arithmetic operator
z1 = x1 + y1
print(z1)


# In[356]:


print(type(x1))
print(type(y1))


# In[357]:


x1 = input('Enter the 1st number') #whenevery you works in input function it always give you string 
a1 = int(x1)
y1 = input('Enter the 2nd number') # it wont understand as arithmetic operator
b1 = int(y1)
z1 = a1 + b1
print(z1)


# for the above code notice we are using many lines because fo that wasting some memory spaces as well

# In[ ]:


x2 = int(input('Enter the 1st number'))
y2 = int(input('Enter the 2nd number'))
z2 = x2 + y2
z2


# lets take input from the user in char format, but we dont have char format in python

# In[358]:


ch = input('enter a char')
print(ch)
#print(type(ch))


# In[359]:


print(ch[0])


# In[360]:


print(ch[0:2])


# In[361]:


print(ch[1])


# In[362]:


print(ch[-1])


# In[363]:


ch = input('enter a char')[0]
print(ch)


# In[364]:


ch = input('enter a char=')[1:3]
print(ch)


# LETS UNDERSTAND THE CONDITION TO COMPUTER TO THINK FOR THAT WE HAVE SOME SPECIAL KEYWORD -
# 1]if
# 2]if else
# 3]if elif else 
# 4]nested if

# In[367]:


if True: # indentiation is always 4 spaces
    print('Data Science')


# In[368]:


if False:
    print('Data Science')
print('bye for now')


# In[369]:


if True: # indentiation is always 4 spaces
    print('Data Science')
print('bye for now')


# Lets do one program as if divide by 2 then reminder is 0 then it is even number if reminder is not 0 then it is odd number

# In[370]:


#to print only even number
x = 4
r = x % 2 
if r == 0:
    print('Even number')


# In[371]:


#to print only even number
x = 5
r = x % 2 
if r == 0:
    print('Even number')


# In[372]:


x = 5
r = x % 2 
if r == 0:
    print('Even number')
print('odd number')


# In[373]:


x = 8
r = x % 2 
if r == 0:
    print('Even number')
print('odd number')


# In[374]:


x = 8
r = x % 2 
if r == 0:
    print('Even number')
if r == 1:
    print('odd number')


# In[375]:


x = 7
r = x % 2 
if r == 0:
    print('Even number')
if r == 1:
    print('odd number')


# In[376]:


x = 15
r = x % 2 
if r == 0:
    print('Even number')
if r != 0:
    print('odd number')


# if we observe the code its too many line cuz many of the coder always they wanted to reduce the code lenght which is very good practise. instead of 2 if we can use if-- else

# In[377]:


x = 5
r = x % 2
if r == 0:
    print('Even number')
else:
    print('Odd Number')


# In[378]:


x = 4
r = x % 2
if r == 0:
    print('Even number')
else:
    print('Odd Number')


# In[379]:


x = 3
r = x % 2
if r == 0:
    print(' Even number')
    if x>5:
        print('greater number')
else:
    print('Odd Number')


# In[380]:


x = 4
r = x % 2
if r == 0:
    print('Even number')
    if x>5 :
        print('greater number')
    else:
        print('not greater ')
else:
    print('odd number')


# In[381]:


x = 6
r = x % 2
if r == 0:
    print('Even number')
    if x>5 :
        print('greater number')
    else:
        print('not greater ')
else:
    print('odd number')


# We do have concept of ( IF - ELIF- ELSE) e.g i want to print ( 1--> one , 2 --> two, 3--> three, 4--> four, 5- five)

# In[382]:


x = 3

if x == 1:
    print('one')
if x == 2:
    print('Two')
if x == 3:
    print('Three')
if x == 4:
    print('four')


# In[383]:


x = 1

if(x == 1):
    print('one')
elif(x == 2):
    print('Two')
elif(x == 3):
    print('Three')
elif(x == 4):
    print('four')


# In[384]:


x = 7

if(x == 1):
    print('one')
elif(x == 2):
    print('Two')
elif(x == 3):
    print('Three')
elif(x == 4):
    print('four')


# In[385]:


x = 7

if(x == 1):
    print('one')
elif(x == 2):
    print('Two')
elif(x == 3):
    print('Three')
elif(x == 4):
    print('four')
else:
    print('wrong output')


# In[386]:


x = 10

if(x == 1):
    print('one')
elif(x == 2):
    print('Two')
elif(x == 3):
    print('Three')
elif(x == 4):
    print('four')
else:
    print('wrong output')


# LOOPS -- in programing world some time we keep on repeating , may be you want to repeat 5 statement so one way is copy & paste multiple times or other way is
# 
# if you want to print the datascience 1000 times then what you will you cant copy for 1000 times , if you want to print 1000 times then you cant do manualy . that is the reason why we need to apply loop -> 2 type of loops -- While loop & For loop

# In[387]:


print('data science')
print('data science')
print('data science')
print('data science')    
print('data science')


# In[388]:


i = 1          # initializing
while i<=5:    # condition
    print('data science')
    i = i + 1  # increment


# In[389]:


i = 5          # initializing
while i>=1:    # condition
    print('data science')
    i = i - 1  # decrement


# In[390]:


i = 1         # initializing
while i<=5:    # condition
    print('data science',i)
    i = i + 1  # increment


# In[391]:


i = 5          # initializing
while i>=1:    # condition
    print('data science',i)
    i = i - 1  # decrement


# In[392]:


i = 1
while i<=5:
    print('data science') # when we mention end then new line will not create
    j = 1
    while j<=4:
        print('technology')
        j = j + 1
        
    i = i + 1
    print()
    


# In[393]:


i = 1
while i<=5:
    print(' datascience', end = "") # when we mention end then new line will not create
    j = 1
    while j<=4:
        print(' technology', end="")
        j = j + 1
        
    i = i + 1
    print()


# In[394]:


# lets use while loop usig some numbers
i = 1
while i <= 2 :
    j = 0
    while  j <= 2 :
        print(i*j, end=" ")
        j += 1
    print()
    i += 1


# In[395]:


# lets use while loop usig some numbers
i = 1
while i <= 4 :
    j = 0
    while  j <= 3 :
        print(i*j, end=" ")
        j += 1
    print()
    i += 1


# FOR LOOP - normally while loop it work with iteration or certaion some condition but for loop it will work with sequence (list, string,int)

# In[396]:


name = 'nit'
for i in name:
    print(i)


# In[397]:


name = 'nit'
for i in name:
    print(i,end=" ")


# In[398]:


name1 = [1,3.5,'hallo'] #i want print the value individualy
for i in name1:
    print(i)


# In[399]:


for i in [2, 3, 7.8, 'hi']:
    print(i)


# In[400]:


for i in range(5):
    print(i)


# In[401]:


for i in range(1,5):
    print(i)


# In[402]:


for i in range(1,10,3):
    print(i)


# In[403]:


# print the value which is divisible by 5 
for i in range(1,21):
    if i%5==0 :
        print(i)


# In[404]:


# print the value which is divisible by 5 i dont want that value 
for i in range(1,21):
    if i%5!=0 :
        print(i)


#  LETS DISCUSS ABOUT 3 KEYWORDS -- BREAK || CONTINUE || PASS BREAK STATEMNT - if you apply break statment in a loop then it will end the loop # Pass = skips block of code( function, class etc) # Continue= skips 1 step/iteration during loop # Break= jumps out of the function/loop
# 
#  

# In[405]:


# write the code user ask chocklet from vendor machne write the basic code 

x = int(input('How many choclets you want:?'))

i = 1
while i<=x:
    print('choclet')
    i += 1       


# In[406]:


ava = 5 # the machine has only 5 choclet 

x = int(input('How many choclets you want:?'))

i = 1
while i<=x:
    print('choclet')
    i += 1   
# if you check the user wants 10 choclets  but availabe choclet is 5 but we got output as 10 choclet
# in this code we just declare but we dint apply any condition to it 


# In[407]:


available_choclet = 5 # the machine has only 10 candis 

x = int(input('How many choclets you want:?'))

i = 1
while i<=x:
    
    if i>available_choclet: # we stop the execution but which code execution not entire code , i want to come out of while loop 
        break # break is statement | means jump out of the loop
    print('choclet')
    i += 1   
    
print('bye for now')


# In[408]:


available_choclet = 5 # the machine has only 10 candis 

x = int(input('How many choclets you want:?'))

i = 1
while i<=x:
    
    if i>available_choclet: # we stop the execution but which code execution not entire code , i want to come out of while loop 
        print('out of stock')
        break # break is statement | means jump out of the loop
    print('choclet')
    i += 1   
    
print('bye for now')


# In[409]:


for i in range(1,11):
    print(i)


# i dont want 11 number i want only 5 number for the range of 1 to 10

# In[410]:


for i in range(1,11):
    if i == 5:
        break 
    print(i)


# In[411]:


for i in range(1,11):
    if i == 3:
        continue 
    print(i)


# In[412]:


for i in range(1,11):
    if i == 5:
        continue 
    print('hello ',i)    


# #PASS Statement - pass the code & it wont go ( code give you the error)

# In[413]:


for i in range(1,11):     


# In[414]:


for i in range(1,11):
    pass


# you need to print the number from 1 to 50 but dont print the value which is divisible by 3 or 5

# In[415]:


for i in range(1,50):
    if i%3 == 0:
        print(i)
print('end')   


# In[416]:


for i in range(1,50):
    if i%3 == 0:
        continue
    print(i)
print('end')    


# In[417]:


for i in range(1,50):
    if i%3 == 0 or i%5 == 0:
        continue
    print(i)
print('end')    
# it will skip all the value which is divisible by 3 or 5


# In[418]:


for i in range(1,50):
    if i%3 == 0 and i%5 == 0:
        continue
    print(i)
print('end')    
# when you apply and you wont get the value which is divisible by both 3 & 5 (15)


# In[419]:


# i dont want to print the values which are odd numbers that means print only even numbers
for i in range(1,50):
    
    if (i%2 != 0):
        pass
    else:
        print(i)
print('bye')


# In[420]:


# PRINTING PATTERN IN PYTHON


# In[421]:


print('# # # #')
print('# # # #')
print('# # # #')
print('# # # #')


# In[422]:


for j in range(4):
    print('#')


# In[423]:


for j in range(4):
    print('#', end=" ")


# In[424]:


for j in range(4):
    print('#', end=" ")

for j in range(4):
    print('#', end=" ")


# In[425]:


for j in range(4):
    print('#', end=" ")
    
print()
    
for j in range(4):
    print('#', end=" ")


# In[426]:


for j in range(4):
    print('#', end="  ")
    
print()

for j in range(4):
    print('#', end="  ")

print()

for j in range(4):
    print('#', end="  ")
    
print()

for j in range(4):
    print('#', end="  ")


# In[427]:


for i in range(7):
    for j in range(4):
        print('#', end="  ")
    print()


# In[428]:


list(range(5))


# In[429]:


for i in range(5):
    for j in range(i):
        print('#', end="  ")
    print()


# In[430]:


for i in range(1,6):
    print('$'*i)


# In[431]:


for i in range(5):
    for j in range(i+1):
        print('#',end="  ")
    print()


# In[432]:


for i in range(4):
    for j in range(4-i):
        print('#', end="  ")
    print()


# For|Else in python
# In other language for else not supportable but in python it is supportable
# eg- lets print the number from 1- 20 & we dont want print number which is divisible by 

# In[433]:


nums = [12,15,18,21,26]
for num in nums:
    if num % 5 == 0:
        print(num)  


# In[434]:


nums = [12,14,18,21,25,30,35]
for num in nums:
    if num % 5 == 0:
        print(num)  


# In[435]:


nums = [12,14,18,21,25,20]
for num in nums:
    if num % 5 == 0:
        print(num) 


# In[436]:


nums = [12,14,18,21,25,20]
for num in nums:
    if num % 5 == 0:
        print(num)  
        break


# In[437]:


nums = [12,14,18,21,20,25]
for num in nums:
    if num % 5 == 0:
        print(num)  
        break


# In[438]:


nums = [10,14,18,21,5,10]
for num in nums:
    if num % 5 == 0:
        print(num)  
        break #it will print only 1 number then it bre


# In[439]:


nums = [10,14,18,21,25,20]
for num in nums:
    if num % 5 == 0:
        print(num)  
      


# In[440]:


nums = [7,14,18,21,23,27] #hear there is no number which is divisible by 5 we got output as blank
for num in nums:
    if num % 5 == 0:
        print(num)  
        break


# In[441]:


nums = [7,14,18,21,23,27] #hear there is no number which is divisible by 5 we got output as blank
for num in nums:
    if num % 5 == 0:
        print(num)  
        break
    else:
        print('Number Not Found') #every iteration it cheking condition       


# In[442]:


nums = [7,14,18,20,23,27] #hear there is no number which is divisible by 5 we got output as blank
for num in nums:
    if num % 5 == 0:
        print(num)  
        break
    else:
        print('Number Not Found') #every iteration it cheking condition       


# In[443]:


nums = [7,14] #hear there is no number which is divisible by 5 we got output as blank
for num in nums:
    if num % 5 == 0:
        print(num)  
        break
    else:
        print('Number Not Found') #every iteration it cheking condition        


# In[444]:


nums = [7,14,18,28,23,27] #hear there is no number which is divisible by 5 we got output as blank
for num in nums:
    if num % 5 == 0:
        print(num)  
        break
else:
        print('Number Not Found') # hear else we dont write in if block but we can write in for block only


# In[445]:


nums = [18,14,18,21,20,27] #hear there is no number which is divisible by 5 we got output as blank
for num in nums:
    if num % 5 == 0:
        print(num)  
        break
else:
        print('Not Found')


# In[446]:


nums = [10,14,18,21,20,27,30] #hear there is no number which is divisible by 5 we got output as blank
for num in nums:
    if num % 5 == 0:
        print(num)  
        #break
else:
        print('Not Found')


# In[447]:


nums = [10,14,18,21,20,27] #hear there is no number which is divisible by 5 we got output as blank
for num in nums:
    if num % 5 == 0:
        print(num)  
        break
else:
        print('Not Found')


# prime number - how to check given number is prime number or not

# In[448]:


num = 12
for i in range(2,num):
    if num % i == 0:
        print('Not prime Number')
        break
else:
    print('Prime Number')


# In[449]:


num = 13
for i in range(2,num):
    if num % i == 0:
        print('Not prime Number')
        break
else:
    print('Prime Number')


# In[450]:


from array import * 
arr = array('i',[])

n = int(input('Enter the length of the array'))

for i in range(5):
    x = int(input('Enter the next value'))
    arr.append(x)
print(arr)


# In[454]:


# Way of creating array using numpy


# In[455]:


from numpy import *
arr = array([1,2,3,4,5])
print(arr)
type(arr)


# In[456]:


print(arr.dtype)


# In[457]:


arr = array([1,2,3,4.0,5])
print(arr)


# In[458]:


print(arr.dtype)


# In[459]:


arr2 = array([1,2,3,4,5.9],float)
arr2


# In[460]:


arr3 = array([1,2,3,4,5.6],int)
arr3


# In[461]:


import numpy as np


# In[462]:


arr4 = np.linspace(0, 16, 10) # break the code between 10 spaces between 0 to 16 but why decimal becuase we break into parts thats why it is floats
arr4


# In[463]:


arr5 = np.arange(0,10,2) # arange - as range
arr5


# In[464]:


arr6 = np.zeros(5)
arr6


# In[465]:


arr7 = np.ones(5)
arr7


# In[ ]:





# In[ ]:




