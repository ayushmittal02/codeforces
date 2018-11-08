
# coding: utf-8

# In[3]:


s=input()
l=list(s)
l1=list()
l2=list()
for i in range (len(l)):
    if l[i]!='+':
        l1.append(l[i])
l1=sorted(l1)
for j in range (len(l1)):
    if j==(len(l1)-1):
        l2.append(l1[j])
    else:
        l2.append(l1[j])
        l2.append('+')
s=''.join(l2)
print(s)

