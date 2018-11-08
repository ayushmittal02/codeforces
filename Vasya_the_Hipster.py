
# coding: utf-8

# In[3]:


l=list(map(int,input().split()))
if l[0]>l[1]:
    x=l[0]-l[1]
    s1=l[1]
    if x==1:
        s2=0
    else:
        s2=x//2
elif l[0]<l[1]:
    x=l[1]-l[0]
    s1=l[0]
    if x==1:
        s2=0
    else:
        s2=x//2
else:
    s1=l[0]
    s2=0
print(s1,end=" ")
print(s2)

