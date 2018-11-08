
# coding: utf-8

# In[3]:


n=int(input())
a1=0
a2=0
a3=0
for i in range (n):
    l=list(map(int,input().split()))
    a1=a1+l[0]
    a2=a2+l[1]
    a3=a3+l[2]
if a1==0 and a2==0 and a3==0:
    print("YES")
else:
    print("NO")

