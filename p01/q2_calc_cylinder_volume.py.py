
# coding: utf-8

# In[ ]:


import math

length = float(input("Length in meters:"))
radius = float(input("Radius in meters:"))
area = radius * radius * math.pi
volume = area * length
print(volume)

