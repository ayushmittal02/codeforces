
# coding: utf-8

# In[4]:


n=int(input())
l=list(map(int,input().split()))
l=sorted(l)
x=0
for i in range (n-1):
    a=l[-1]-l[i]
    x=x+a
print(x)

