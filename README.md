

<img src='http://www.kudosdata.com/wp-content/uploads/2016/11/cropped-KudosLogo1.png' width=20% style="float: right;">
# Workshop Blog Installation Guide
### http://www.KudosData.com

by: Sam.Gu@KudosData.com


April 2017

---

# Option 1: Use Cloud Platform (Difficulty level: Easy, like being a boss)

### Create an account in Google Cloud Platform (GCP), using Cloud Console

### Start Datalab (Jupyter python notebook) in GCP Compute Engine, using Cloud Shell

### Create a new notebook from datalab folder, then run below two command in notebook cell:

!git clone https://github.com/telescopeuser/workshop_blog.git


%load workshop_blog/setup_cloud.py (run the cell twice: 1st to load WeChat API installtion code; 2nd to install/)


### [Environment setup is now completed, Yeah~]

---

# Option 2: Use a Virtual Machine to run in your own computer (Difficulty level: Medium, as bribing your colleague)

### Download a virtual machine (VM about 1.5 GB), which contains this workshop notebook.
To be announced... or email me for enquiry: Sam.Gu@KudosData.com


### Install Virtualbox tool to use above virtual machine, if you don't have this software. https://www.virtualbox.org/wiki/Downloads

### Start to run the VM using Virtualbox (Check Host-VM network setting if needed.)

### [Optional] Update workshop python notebook code from Github: https://github.com/telescopeuser/workshop_blog.git

### Open a web browser, go to url: http://127.0.0.1:8080/tree

### [Environment setup is now completed, Yeah~]

---

# Option 3: Use your own computer (Difficulty level: High, as what you normally do)

### Install Anaconda (This software includes many useful tools: Python, Jupyter Notebook, pip)
https://www.continuum.io/downloads

### Install WeChat API package for Anaconda3 / python3+ (Recommended)

* pip install -U wpxy

### Install WeChat API package for Anaconda2 / python2+  (Not Recommended)

* Download wxpy from Github: https://github.com/telescopeuser/wxpy.git
* Go to command line: python setup.py install
* Go to command line: pip uninstall itchat


* Download itchat from Github: https://github.com/telescopeuser/ItChat.git
* Go to command line: python setup.py install


* pip install -U some packages: html, backports.tempfile


### Download workshop python notebook code from Github: https://github.com/telescopeuser/workshop_blog.git

### Start Jupyter Notebook (Here I use Git Bash command line tool)

### Open a webbrowser, go to url: http://localhost/tree

### [Environment setup is now completed, Yeah~]

---

# After completing one of the installation options, you are now ready to rock! Go to folder: workshop_blog/wechat_tool, open Notebook and follow...

<img src='./wechat_tool/reference/setup_ref_01.png' width=100% style="float: left;">

---
