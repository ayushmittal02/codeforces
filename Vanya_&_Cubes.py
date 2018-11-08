
# coding: utf-8

# In[16]:


n=int(input())
sum=0
i=1
x=0
a=i+x
if n==1:
    print("1")
else:
    while n>0 and n>a:
        sum=sum+1
        a=i+x
        x=x+(i+x)
        n=n-a
        i=i+1
    print(sum)

