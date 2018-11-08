
# coding: utf-8

# In[4]:


l=list(map(int,input().split()))
l1=list()
l1.append(l[0])
for i in range (1,len(l)):
    if l[i] not in l1:
        l1.append(l[i])
print(4-len(l1))

