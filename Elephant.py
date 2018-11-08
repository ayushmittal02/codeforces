
# coding: utf-8

# In[2]:


n=int(input())
x=0
while n>0:
    if (n%5)==0:
        x=x+1
        n=n-5
    else:
        if (n%4)==0:
            x=x+1
            n=n-4
        else:
            if (n%3)==0:
                x=x+1
                n=n-3
            else:
                if (n%2)==0:
                    x=x+1
                    n=n-2
                else:
                    x=x+1
                    n=n-1
print(x)

