
# coding: utf-8

# In[ ]:


N=int(input())
for i in range (N):
    s=input()
    l=list(s)
    if len(l)>10:
        l1=list()
        l1.append(l[0])
        l1.append(str(len(l)-2))
        l1.append(l[-1])
        x=''.join(l1)
        print(x)
    else:
        print(s)

