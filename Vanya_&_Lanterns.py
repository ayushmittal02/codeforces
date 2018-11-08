
# coding: utf-8

# In[6]:


n=list(map(int,input().split()))
l=list(map(int,input().split()))
l=sorted(l)
x=max(l[0],(n[1]-l[-1]))
for i in range (n[0]-1):
    if ((l[i+1]-l[i])/2)>x:
        x=(l[i+1]-l[i])/2
print(x)

