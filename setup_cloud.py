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

get_ipython().system('python --version')


# In[ ]:

get_ipython().system('pip install -U html')


# In[ ]:

get_ipython().system('pip install -U pyqrcode')


# In[ ]:

get_ipython().system('pip install -U config')


# In[ ]:

get_ipython().system('pip install -U backports.tempfile')


# In[ ]:

get_ipython().system('mv docs org_docs')


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
get_ipython().system('rm -rf docs*')
get_ipython().system('rm -rf requirements.txt')
get_ipython().system('rm -rf setup.py')
get_ipython().system('rm -rf *.egg-info')

get_ipython().system('mv org_docs docs')


get_ipython().system('pip install -U google-api-python-client')
get_ipython().system('pip install -U gTTS')
get_ipython().system('apt-get update -y')

# 21 Dec 2017: update: '--allow-unauthenticated', thanks to: MENG EN
# get_ipython().system('apt-get install libav-tools -y')
get_ipython().system('apt-get install libav-tools -y --allow-unauthenticated')

get_ipython().system('avconv -version')


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



