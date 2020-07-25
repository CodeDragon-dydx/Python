
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


# In[ ]:



