
# coding: utf-8

# In[2]:

print("Hello World")


# In[3]:

a = 3
A = 4
print(a)
print(A)


# In[5]:

a = 3
b = 9
if b%a == 0:
    print("b is divisible by a")
elif b+1 == 10:
    print("increment in b produces 10")
else:
    print("you are in else statement")


# In[6]:

def checkDivisibility(a,b):
    if a%b == 0:
        print("a is divisible by b")
    else:
        print("a is not divisible by b")
    
checkDivisibility(4,2)


# In[7]:

x = 10;
print(type(x))

x =100000000000000000000000000000000
print(type(x))


# In[10]:

def f():
    print(s)

s = "I love Geekforgeeks"
f()


# In[12]:

def f():
    s = "me too.
    print(s)
    
s = "I love Geekforgeeks"
f()
print(s)


# In[14]:

def f():
    global s
    print(s)
    s = "Me too."
    print(s)

s ="I love Geekforgeeks."
f()
print(s)


# In[15]:

def f():
    print("inside f:",a)
def g():
    a= 2
    print("inside g:",a)
def h():
    global a
    a = 3
    print("inside h:",a)
    
#global scope

print('global:', a)
f()
print('global:', a)
g()
print('global:',a)
h()
print('global:',a)


# In[16]:

def fun(a,b,c,d):
    print(a,b,c,d)
    
my_list = [1,2,3,4]

fun(*my_list)


# In[17]:

range(3,6)

args = [3,6]
range(*args)


# In[18]:

def mySum(*args):
    sum = 0
    for i in range(0, len(args)):
        sum += args[i]
    return sum

print(mySum(1,2,3,4,5))
print(mySum(10,20))


# In[2]:

def fun1(a,b,c):
    print(a,b,c)
    
def fun2(*args):
    args = list(args)
    
    args[0] = "Geeksforgeeks"
    args[1] = "awesome"
    
    fun1(*args)
    
fun2('Hello', 'beautiful', 'world!')


# In[3]:

def fun1(a,b,c):
    print(a,b,c)
    
d = {'a':2, 'b':4, 'c':10}
fun1(**d)


# In[4]:

def fun(**kwargs):
    print(type(kwargs))
    
    for key in kwargs:
        print("%s = %s" %(key, kwargs[key]))
        
fun(name = "geeks", ID = "101", language = "Python")


# In[ ]:



