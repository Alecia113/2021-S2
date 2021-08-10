#!/usr/bin/env python
# coding: utf-8

# In[20]:


import torch
x = torch.rand(5, 3)
print(x)


# In[ ]:


# #esc+其他
# https://blog.csdn.net/yiyue21/article/details/96577163?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522162849129316780271544744%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=162849129316780271544744&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_v2~rank_v29-3-96577163.first_rank_v2_pc_rank_v29&utm_term=jypter+加块的快捷键&spm=1018.2226.3001.4187


# In[31]:


#https://download.pytorch.org/whl/torch_stable.html
get_ipython().system('pip install torch-1.9.0-cp36-none-macosx_10_9_x86_64.whl')


# In[23]:


import torch
torch.__version__


# In[32]:


print(torch.version.cuda)


# In[34]:



import torch
torch.cuda.is_available()
#https://blog.csdn.net/weixin_39932947/article/details/111157914?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_utm_term~default-0.control&spm=1001.2101.3001.4242
# 装了好几天的环境，死活用不了GPU
# torch.cuda.is_available()返回结果一遍一遍的都是False，心态都崩了！！！
# 一开始以为是nvidia驱动的问题，然后看了几篇帖子，总结一下我的错误


# In[ ]:


def f(n):
    if n == 1:
        return 1
    else:
        return n*f(n-1)
number = int(input('zhengzhengshu:'))
result = f(number)
print("%d:%d"%(number, result))
# com+shift+p 命令面板

# Anaconda Navigtor ：用于管理工具包和环境的图形用户界面，后续涉及的众多管理命令也可以在 Navigator 中手工实现。

# Jupyter notebook ：基于web的交互式计算环境，可以编辑易于人们阅读的文档，用于展示数据分析的过程。

# qtconsole ：一个可执行 IPython 的仿终端图形界面程序，相比 Python Shell 界面，qtconsole 可以直接显示代码生成的图形，实现多行代码输入执行，以及内置许多有用的功能和函数。

# spyder ：一个使用Python语言、跨平台的、科学运算集成开发环境。

# 安装完成后，我们还需要对所有工具包进行升级，以避免可能发生的错误。打开你电脑的终端，在命令行中输入：

# conda upgrade --all

# 在终端询问是否安装如下升级版本时，输入 y。

# 有的情况下，你可能会遇到找不到 conda 命令的错误提示，这很可能是环境路径设置的问题，需要添加conda环境变量：export PATH=xxx/anaconda/bin:$PATH, 其中xxx替换成anaconda的安装路径。

# 至此，安装完成，下面让我们看一下如何用 Anaconda 管理工具包和环境。

# 1.Edit 编辑command + / 注释

# command + W 快速选择

# command + C Copy, 复制

# command + shift + C 复制路径

# command + V 粘贴

# command + shift + V 从剪贴板中粘贴

# command + Y 删除整行

# shift + Backspace 删除整行

# Alt + Backspace 删除整个单词

# command + X 剪切

# command + Z 撤回修改

# command + shift + Z 重做修改

# command + D Duplicate, 重复内容


# In[ ]:


#https://blog.csdn.net/anu77781/article/details/101159748?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522162848181716780357276378%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=162848181716780357276378&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-2-101159748.first_rank_v2_pc_rank_v29&utm_term=jupyter+notebook快捷键&spm=1018.2226.3001.4187
import matplotlib.pyplot as plt
import numpy as np


# In[5]:


#


# In[ ]:


3##

