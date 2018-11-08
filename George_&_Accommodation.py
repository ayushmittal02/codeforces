
# coding: utf-8

# In[2]:


n=int(input())
ans=0
for i in range (n):
    l=list(map(int,input().split()))
    temp=l[1]-l[0]
    if temp>1:
        ans=ans+1
print(ans)

