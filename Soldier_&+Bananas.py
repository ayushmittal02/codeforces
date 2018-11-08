
# coding: utf-8

# In[6]:


l=list(map(int,input().split()))
amount=0
temp=1
for i in range (l[2]):
    amount=amount+(temp*l[0])
    temp=i+2
ans=amount-l[1]
if ans<0:
    print("0")
else:
    print(ans)

