
# coding: utf-8

# In[5]:


s=input()
l=list(s)
x1=0
x2=0
for i in range (len(l)):
    if l[i].isupper()==True:
        x1=x1+1
    else:
        x2=x2+1
if x1<=x2:
    s=s.lower()
else:
    s=s.upper()
print(s)

