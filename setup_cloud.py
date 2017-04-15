
# coding: utf-8

# 
# <img src='http://www.kudosdata.com/wp-content/uploads/2016/11/cropped-KudosLogo1.png' width=20% style="float: right;">
# # Workshop Blog Installation Guide
# ### http://www.KudosData.com
# 
# by: Sam.Gu@KudosData.com
# 
# 
# April 2017

# # Option 1: Use Cloud Platform (Difficulty level: Easy, like being a boss)

# In[ ]:

get_ipython().system('python --version')


# In[ ]:

get_ipython().system('pip install -U html')


# In[ ]:

get_ipython().system('pip install -U pyqrcode')


# In[ ]:

get_ipython().system('pip install -U config')


# In[ ]:

get_ipython().system('pip install -U backports.tempfile')


# ### Download and install WeChat API-1

# In[ ]:

get_ipython().system('yes | pip uninstall wxpy')
get_ipython().system('rm -rf wxpy')
get_ipython().system('git clone https://github.com/telescopeuser/wxpy.git')
get_ipython().system('cp -r wxpy/* .')
get_ipython().system('python setup.py install')


# ### Download and install WeChat API-2

# In[ ]:

get_ipython().system('yes | pip uninstall itchat')
get_ipython().system('rm -rf ItChat')
get_ipython().system('git clone https://github.com/telescopeuser/ItChat.git')
get_ipython().system('cp -r ItChat/* .')
get_ipython().system('python setup.py install')


# ### Housekeeping after installation

# In[ ]:

get_ipython().system('rm -rf itchat')
get_ipython().system('rm -rf ItChat')
get_ipython().system('rm -rf wxpy')
get_ipython().system('rm -rf README*')
get_ipython().system('rm -rf LICENSE')
get_ipython().system('rm -rf MANIFEST*')
get_ipython().system('rm -rf mkdocs*')
get_ipython().system('rm -rf build')
get_ipython().system('rm -rf dist')
get_ipython().system('rm -rf requirements.txt')
get_ipython().system('rm -rf setup.py')
get_ipython().system('rm -rf *.egg-info')


# ### Reset/Restart Session to make installation effective

# In[ ]:

# from wxpy import *


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



