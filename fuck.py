# -*- coding: utf-8 -*-

import mysql.connector
mydb = mysql.connector.connect(
  host="192.168.10.247",
  user="root",
  passwd="spadec",
  database="auth"
)
street = "улица Дачная"
f = open('read.txt' , 'r', encoding='utf-8')
listValues = []
listValues = f.read().split(';')
# print(listValues)
streets = []
obj={
    'name':"" , 'arr':""
}
mycursor = mydb.cursor()
for sub in listValues:
    obj['name'] = sub[0:sub.find(':'):1].replace('\n','')
    obj['arr'] = sub[sub.find(':')+1::1]
    obj['arr'] = obj['arr'].replace(' ' , '').split(',')
    street = obj['name']
    for nums in obj['arr']:
        num=nums
        sql = "call iadr('%s', '%s',184)" % (street,num)
        print(sql)
        mycursor.execute(sql)
# for i in listValues:
#     
#     # val = (i)
#     print(i)


        
f.close()
mydb.commit()