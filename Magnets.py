
# coding: utf-8

# In[4]:


n=int(input())
l=list()
x=1
for i in range (n):
    s=input()
    l.append(s)
for j in range (n-1):
    if l[j]!=l[j+1]:
        x=x+1
print(x)


# # 
