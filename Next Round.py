
# coding: utf-8

# In[3]:


n=list(map(int,input().split()))
l=list(map(int,input().split()))
x=l[n[1]-1]
l1=list()
for i in range (n[0]):
    if l[i]>=x and l[i]>0:
        l1.append(l[i])
print(len(l1))

