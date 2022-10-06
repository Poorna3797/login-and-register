#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re

class Registration:

  def __init__(self):
    self.db=open('data1.txt','wb')
    self.db.close()

  def Email(self):
    email_cond='[A-Za-z0-9_+*]+@[A-Za-z0-9]+\.[A-Za-z]{2,}'
    while True:
      try:
        print('\nEmail/username: ')
        self.Ename=input()
        if re.search("^[0-9@$!%*#?&]",self.Ename):
          print("invalid Email\nPlease enter a valid Email address")
        else:
          if(re.fullmatch(email_cond,self.Ename)):
            break
      except:
        print("invalid Email. Please provide a valid Email address")
        continue
  
  def Password(self):
    pass_cond= "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{5,16}$"
    while True:
      try:
        print('\nPassword: ')
        self.Passwd=input()
        if re.fullmatch(pass_cond,self.Passwd):
          break
      except:
        print("invalid password. Please provide a valid password")
        continue

  def store(self,Ename,Passwd):
    self.db=open("data1.txt",'a')
    self.db.write(self.Ename+","+self.Passwd+"\n")
    self.db.close()

  def login(self,Ename,Passwd):
    self.db=open("data1.txt","r")
    for i in self.db:
      self.a,self.b = i.split(",")
      self.b=self.b.strip()
      if(self.a==self.Ename and self.b==self.Passwd):
        print("Login Successful. Welcome "+self.Ename)
        break
      elif(self.a==self.Ename and self.b!=self.Passwd):
        print("\nIncorrect Password. \n1) Forget Password\n2) exit")
        option=int(input())
        if option==1:
          print("\n1) Retrieve old password\n2) new password")
          self.opt=int(input())
          if self.opt==1:
            print("\npassword: ", self.b)
            break
          elif self.opt==2:
            print("\nEnter new password: ")
            self.new_passwd=input()
            self.db=open("data1.txt","r")
            self.data = self.db.read()  
            self.data = self.data.replace(self.b,self.new_passwd)       
            self.db=open("data1.txt","w")
            self.db.write(self.data)
            print("\npassword changed")
            break
          elif option==2:
            break
      else:
        print("Wrong username or it doesn't exist. Please select registeration to create a username and password to login")
        break
    self.db.close()


# In[2]:


reg=Registration()


# In[ ]:


print("\nIf you don't have username and password please select registration to create your username and password to login")
while True:
  print("\n***************Please select from below options***************")
  print('\n1) Login\n2) Registration\n3) exit')
  option=int(input())
  if option == 1:
    ename=reg.Email()
    passwd=reg.Password()
    reg.login(ename,passwd)
  elif option == 2:
    ename=reg.Email()
    passwd=reg.Password()
    reg.store(ename,passwd)
    print('\nProfile created successfully')
  elif option ==3:
    break


# In[ ]:




