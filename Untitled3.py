#!/usr/bin/env python
# coding: utf-8

# In[1]:


first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# print the full name in reverse order
print(last_name + " " + first_name)


# In[2]:


n = int(input("Enter an integer: "))

# compute n+nn+nnn
result = n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n))

# result
print("The result is:", result)


# In[3]:


# get  number
num = int(input("Enter a number: "))

# check even or odd
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")


# In[4]:



nums = []

for num in range(2000, 3201):
    # check if the number is divisible by 7 and not a multiple of 5
    if num % 7 == 0 and num % 5 != 0:
        # append the number to the list of numbers
        nums.append(num)

# print the list of numbers on a single line
print(*nums, sep=", ")


# In[5]:


# get the original price
price = float(input("Enter the price: "))

# apply the discount based on the price
if price >= 500:
    discounted_price = price * 0.5
elif price >= 200:
    discounted_price = price * 0.7
else:
    discounted_price = price * 0.9

# display the discounted price to the user
print("The discounted price is:", discounted_price)


# In[ ]:




