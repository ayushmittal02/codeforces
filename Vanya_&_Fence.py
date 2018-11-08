
# coding: utf-8

# In[3]:


l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
x=0
for i in range (len(l2)):
    if l2[i]>l1[1]:
        x=x+2
    else:
        x=x+1
print(x)

