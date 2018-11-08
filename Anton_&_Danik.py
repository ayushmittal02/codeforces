
# coding: utf-8

# In[3]:


n=int(input())
s=input()
l=list(s)
x1=0
x2=0
for i in range (n):
    if l[i]=='A':
        x1=x1+1
    else:
        x2=x2+1
if x1>x2:
    print("Anton")
elif x1<x2:
    print("Danik")
else:
    print("Friendship")

