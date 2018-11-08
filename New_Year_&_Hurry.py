
# coding: utf-8

# In[3]:


n=list(map(int,input().split()))
ans=0
x=240-n[1]
for i in range (1,n[0]+1):
    a=5*i
    x=x-a
    if x<0:
        break
    ans=ans+1
print(ans)

