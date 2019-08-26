# -*- coding: utf-8 -*-

import configparser
import ast

config = configparser.ConfigParser()
config.read('config.ini')

#print(config.sections())
for section_list in config.sections():
    print('section_list:',section_list)
    for key in config[section_list] :
       if section_list =='user':
           myusername_list = ast.literal_eval(config.get(section_list,key))
       elif section_list =='pwd':
           mypassword_list=ast.literal_eval(config.get(section_list,key))
       elif section_list =='uid'::
           uid_list=ast.literal_eval(config.get(section_list,key))

#       print(config.get(section_list,key))

print(type(myusername_list),type(mypassword_list),type(uid_list))
print('myusername_list:',myusername_list)
print('mypassword_list:', mypassword_list)
print('uid_list:', uid_list)


"""
myusername_list =["fat1209","k20180317","j20180702"]
mypassword_list =["05161209","20180317k","20180702j"]
uid_list = ["750995","2045238","2053337"]

for i in myusername_list:
  print('myusername_list',i)
"""