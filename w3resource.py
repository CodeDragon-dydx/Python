
# coding: utf-8

# In[1]:

print("Twinkle, twinkle, little star, \n \t How I wonder what you are! \n \t \t Up above the world so high, \n \t \t Like a diamond in the sky. \n Twinkle, twinkle, little star, \n \t How I wonder what you are")


# In[2]:

import sys

print("Python version")

print(sys.version)

print("Version Info")

print(sys.version_info)


# In[3]:

import datetime
now = datetime.datetime.now()
print("Current date and time:")
print(now.strftime("%Y-%m-%d %H:%M:%S"))


# In[1]:

from math import pi

r = float(input("Input the radius of the circle:"))

print("The area of the circle with radius"+str(r)+" is: "+str(pi*r**2))


# In[2]:

fname = input("Enter your first name: ")

lname = input("Enter your last name: ")

print("Hello"+lname+" "+fname)


# In[1]:

values = input("Input some comma seperated numbers:")

list = values.split(",")

tuples = tuple(list)

print("list:", list)

print("tuple:", tuples)


# In[2]:

filename = input("Enter the filename:")

f_extns = filename.split(".")

print("The extension of the file is:"+repr(f_extns[-1]))


# In[ ]:



