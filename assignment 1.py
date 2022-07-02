#!/usr/bin/env python
# coding: utf-8

# 1. Find the approximate change in the value of when 1/x**2 changes from 2 to 100

# In[3]:


from sympy import symbols
from sympy import *
x=symbols('x')
f=1/x**2
df=f.diff(x)
print("Derivate of f=1/x**2 = " ,df)

f1 = lambdify(x, df)
print("The value decreases by - " ,f1(2)*198) #x=x+delta_x -> 200=2+delta_x -> delta_x=198


# 2. Rishi has a total of 590 as currency notes in the denominations of 50, 20 and 10. 
# The ratio of the number of 50 notes and 20 notes is 3:5. 
# If she has a total of 25 notes, how many notes of each denomination she has?
# 

# In[4]:


"""
Assume 50 Rs note be 3x, 20 Rs note will be 5x and 10 Rs note as (25-8x) 
Total denomination=590 
then
50(3x)+20(5x)+10(25-8x)=590 
150x+100x-80x+250=590 
170x=340 
x=2 
50 Rs note are 3x=32=6 
20 Rs note are 5x=52=10 
10 Rs note are 25-16=9.
"""

import sympy as sym
eq=150*x+100*x+250-80*x-590
x=sym.symbols('x')
xv=sym.solve(eq,x)
s=""
for i in xv:
    s+=str(i)

x=int(s)
print(x)

print("50 Rs note are " ,3*x)
print("20 Rs note are " ,5*x)
print("10 Rs note are " ,25-8*x)


# 3. The organizers of an essay competition decide that a winner in the competition gets a prize of 100 
# and a participant who does not win gets a prize of 25. The total prize money distributed is 3,000.
# Find the number of winners, if the total number of participants is 63.

# In[6]:


"""
Let x be the number of winners.

Then participants who do not win is (63 – x)

The prize money given to x winners = Rs ( 100x)

The prize money given to (63 – x) participants is = Rs 25(63 – x)

According to the given data, the total prize money distributed = Rs 3000

Therefore, 100x + 25(63 – x) = 3000 -> x=19
"""
eq=100*x +25*(63-x)-3000
x=sym.symbols('x')
xv=sym.solve(eq,x)
s=""
for i in xv:
    s+=str(i)

x=int(s)
print(x)
print('total no of winners are - ',x)


# 4. The sum of three consecutive multiples of 11 is 363. Find these multiples.

# In[8]:


"""
11x + 11y + 11z = 363
11x + 11(x +1) + 11(x + 2) = 363
33x + 33 = 363
33x = 330
x=10
11(10)=110, 11(10 + 1)=121 and 11(10 + 2)=132
"""

eq=33*x + 33-363
x=sym.symbols('x')
xv=sym.solve(eq,x)
s=""
for i in xv:
    s+=str(i)

x=int(s)
print(x)
print('1st consecutive number - ' ,11*x)
print('2nd consecutive number - ' ,11*(x+1))
print('3rd consecutive number - ' ,11*(x+2))


# 5.The digits of a two-digit number differ by 3. If the digits are interchanged, and the resulting number is added to the original number, we get 143. What can be the original number?

# In[14]:


"""
let the digit be xy diff - x-y=3 ->(eq1) 
numbers are interchanged and the resulting number is added to the original number we get 143 
10x + y + 10y + x = 143 
11x + 11y = 143 
x + y = 13 (eq 2)
"""


from sympy import symbols
x, y = symbols('x y')
eq1=x-y-3
eq2=x+y-13
sol=solve((eq1,eq2),(x,y))  #dict
values=sol.values() #storing values
values_list=list(values) #converting to list
x=values_list[0]
y=values_list[1]
print("the original number is - " + str(x) +str(y) )


# 6. find x

# In[11]:


x=sym.symbols('x')
sym.solve(x+14-6*x+2-7/2,x)


# 7. Find the area of the region included between the parabola y^2 = x and the line x + y = 2
# and the X-axis.

# In[ ]:





# 8. A manufacturer produces three models of toys in the form of bikes say X,Y and Z. 
# Model X takes as 10 man-hour to make per unit, Model Y takes 5 man-hour per unit
# and model Z takes 4 man-hour per unit. There are a total 212 man-hour available per week. 
# Handling and marketing costs are <20, <30 and <40 per unit for models X,Y
# and Z respectively. The total funds available for these purposes are <920 per week. Profits
# per unit for models X,Y and Z are <40, <10and <70 respectively, but at the end of the
# week, company get a profit of <810. Solve the system of equations by matrix method.

# In[17]:


import scipy.linalg as linalg 
import numpy as np
A = np.array([[10, 5, 4],
 [20, 30, 40],
 [40, 10, 70]]) 


B = np.array([212,920,810]) 
print("Solutions:\n",np.linalg.solve(A, B ) )


# 9. inverse trigonometry prove that

# In[ ]:





# In[ ]:




