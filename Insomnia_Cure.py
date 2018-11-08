
# coding: utf-8

# In[10]:


k=int(input())
l=int(input())
m=int(input())
n=int(input())
d=int(input())
l1=list()
x=0
for i in range (1,d+1):
    if ((i%k)==0 or (i%l)==0 or (i%m)==0 or (i%n)==0) and (i not in l1):
        x=x+1
print(x)

