#!/usr/bin/env python
# coding: utf-8

# # Printing

# In[1]:


print(5)


# In[ ]:


#非编辑状态下按下才有用 A forward B backward

print(5)


# In[3]:


print(1,16,1/16,'text')


# In[ ]:


#y: 切换成代码#Shift+M: 合并单元格#H: 查看快捷键 #M mark；#y code
#enter 编辑； #esc 命令上下，蓝色 # 在esc下，上下切换单元格


# In[7]:


print( ' 1 divided by 16 is %f' % (1/16) )
print( ' 1 divided by 16 is %d' % (1/16) ) #’‘中是introduction； 里面的%x是取值模式； 后面%+运算公式
print( ' 1 divided by 16 is %.2f' % (1/16)) #.几x就是保留几位x模式
print( ' 1 divided by 16 is %.2f and 1 divided by 32 is %.2f' %(1/16, 1/32)) #同一个括号里两个运算公式。前面就是两个and %
#但是（）前面依旧是一个%


# # Numbers and Variables 

# In[15]:


a = 1
type(a)
print(type(a))
var1 = 'Welcome to xx'
print(var1, ' is ', type(var1)) #直接打印变量，就是里面的值； ’直接文字‘，type返回类型
b = 10
print(b, 'is ', type(b))
c = 10.0
print(c, 'is', type(c))
d = True
print(d, 'is', type(d))


# In[ ]:





# In[ ]:





# In[ ]:




