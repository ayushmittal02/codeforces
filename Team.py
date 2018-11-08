
# coding: utf-8

# In[2]:


n=int(input())
N=0
for i in range (n):
    l=list(map(int,input().split()))
    x=0
    for j in range (len(l)):
        if l[j]==1:
            x=x+1
    if x>=2:
        N=N+1
print(N)

