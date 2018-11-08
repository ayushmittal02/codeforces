
# coding: utf-8

# In[4]:


l=list(map(int,input().split()))
l1=list()
for i in range (1,l[0]+1):
    if (i%2)!=0:
        l1.append(i)
for j in range (1,l[0]+1):
    if (j%2)==0:
        l1.append(j)
print(l1[l[1]-1])

