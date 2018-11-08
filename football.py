
# coding: utf-8

# In[6]:


s=input()
l=list(s)
ans="NO"
if len(l)>6:
    for i in range (0,len(l)-6):
        if (l[i]=='1' and l[i+1]=='1' and l[i+2]=='1' and l[i+3]=='1' and l[i+4]=='1' and l[i+5]=='1' and l[i+6]=='1') or (l[i]=='0' and l[i+1]=='0' and l[i+2]=='0' and l[i+3]=='0' and l[i+4]=='0' and l[i+5]=='0' and l[i+6]=='0'):
            ans="YES"
print(ans)

