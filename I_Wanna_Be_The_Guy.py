
# coding: utf-8

# In[3]:


n=int(input())
p=list(map(int,input().split()))
q=list(map(int,input().split()))
x=0
for i in range (1,n+1):
    if (i in p[1:]) or (i in q[1:]):
        x=x+1
if x==n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")

