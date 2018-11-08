
# coding: utf-8

# In[5]:


n=list(map(int,input().split()))
s="#Black&White"
for i in range (n[0]):
    l=list(input().split())
    for j in range (n[1]):
        if l[j]=='C' or l[j]=='M' or l[j]=='Y':
            s="#Color"
            break
print(s)

