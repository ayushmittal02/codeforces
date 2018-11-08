
# coding: utf-8

# In[4]:


l=list(map(int,input().split()))
for i in range (10**(l[0]-1),10**(l[0])):
    if (i%l[1])==0:
        x=1
        print(i)
        break
if x!=1:
    print("-1")

