
# coding: utf-8

# In[2]:


n=int(input())
x=0
temp=0
for i in range (n):
    l=list(map(int,input().split()))
    temp=temp+l[1]
    temp=temp-l[0]
    if temp>x:
        x=temp
print(x)

