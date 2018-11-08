
# coding: utf-8

# In[16]:


l=list(map(int,input().split()))
a=l[0]
x=0
while l[0]>0:
    l[0]=l[0]//l[1]
    x=x+l[0]
    if l[0]==1:
        break
if (a%l[1])!=0:
    print(a+x+((a%l[1])-1))
else:
    print(a+x)

