
# coding: utf-8

# In[1]:


n=int(input())
s=input()
s=s.upper()
l=list(s)
l1=list()
l1.append(l[0])
for i in range (1,n):
    if l[i] not in l1:
        l1.append(l[i])
if len(l1)==26:
    print("YES")
else:
    print("NO")

