
# coding: utf-8

# In[3]:


n=list(map(int,input().split()))
x=0
while n[0]<=n[1]:
    n[0]=n[0]*3
    n[1]=n[1]*2
    x=x+1
print(x)

