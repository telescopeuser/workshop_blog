
# coding: utf-8

# # Workshop Installation Guide

# # 如何使用和开发微信聊天机器人的系列教程
# # A workshop to develop & use an intelligent and interactive chat-bot in WeChat

# ### WeChat is a popular social media app, which has more than 800 million monthly active users.
# 
# <img src='http://www.kudosdata.com/wp-content/uploads/2016/11/cropped-KudosLogo1.png' width=30% style="float: right;">
# <img src='wechat_tool/reference/WeChat_SamGu_QR.png' width=10% style="float: right;">
# 
# ### http://www.KudosData.com
# 
# by: Sam.Gu@KudosData.com
# 
# 
# April 2017 ============= Scan the QR code to become trainer's friend in WeChat ===========>>

# # Option 1: Use Cloud Platform (Difficulty level: Easy, like being a boss)

# In[ ]:

get_ipython().system(u'python --version')


# In[ ]:

get_ipython().system(u'pip install -U html')


# In[ ]:

get_ipython().system(u'pip install -U pyqrcode')


# In[ ]:

get_ipython().system(u'pip install -U config')


# In[ ]:

get_ipython().system(u'pip install -U backports.tempfile')


# ### Download and install WeChat API-1

# In[ ]:

# !yes | pip uninstall wxpy
# !rm -rf wxpy
# !git clone https://github.com/telescopeuser/wxpy.git
# !cp -r wxpy/* .
# !python setup.py install


# ### Download and install WeChat API-2

# In[ ]:

get_ipython().system(u'yes | pip uninstall itchat')
get_ipython().system(u'rm -rf ItChat')
get_ipython().system(u'git clone https://github.com/telescopeuser/ItChat.git')
get_ipython().system(u'cp -r ItChat/* .')
get_ipython().system(u'python setup.py install')


# ### Housekeeping after installation

# In[ ]:

get_ipython().system(u'rm -rf itchat')
get_ipython().system(u'rm -rf ItChat')
get_ipython().system(u'rm -rf wxpy')
get_ipython().system(u'rm -rf README*')
get_ipython().system(u'rm -rf LICENSE')
get_ipython().system(u'rm -rf MANIFEST*')
get_ipython().system(u'rm -rf mkdocs*')
get_ipython().system(u'rm -rf build')
get_ipython().system(u'rm -rf dist')
get_ipython().system(u'rm -rf requirements.txt')
get_ipython().system(u'rm -rf setup.py')
get_ipython().system(u'rm -rf *.egg-info')


# ### If above importing has no error, then installation is successful.

# # You are now ready to rock! Go to folder: workshop_blog/wechat_tool, open Notebook and follow...
# 
# <img src='./wechat_tool/reference/setup_ref_01.png' width=100% style="float: left;">

# In[ ]:

print('')
print('+-------------------------------------------------------------------------------------------------+')
print('| www.KudosData.com: Google Cloud Datalab Python 2 setup successful!                              |')
print('| You are now ready to rock! Go to folder: workshop_blog/wechat_tool, open Notebook and follow... |')
print('+-------------------------------------------------------------------------------------------------+')


# In[ ]:


