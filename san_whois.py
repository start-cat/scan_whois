#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import whois

f = open('./dom.txt','r')
for lines in f.readlines():
    try:
        print (lines)
        data = whois.whois(lines.strip())
#       print(data) #去除注释输入完整whois信息
        print ("注册公司：",data.registrar,"注册人：",data.name,"注册邮箱：",data.emails,"注册时间：",data.creation_date,"过期时间：",data.expiration_date)
        print("______________________________")
    except :
        pass
        continue
f.close()
