
# coding: utf-8

# In[5]:


s=input()
l=list(s)
l1=list()
l1.append(l[0])
for i in range (1,len(l)):
    if l[i] not in l1:
        l1.append(l[i])
if (len(l1)%2)==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")

