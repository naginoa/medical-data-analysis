# -*- coding: utf-8 -*-
#分割多个字符
def tsplit(string, delimiters):                     

    delimiters = tuple(delimiters)
    stack = [string,]

    for delimiter in delimiters:
        for i, substring in enumerate(stack):
            substack = substring.split(delimiter)
            stack.pop(i)
            for j, _substring in enumerate(substack):
                stack.insert(i+j, _substring)

    return stack
	
calc3=1
while (calc3<=13):
 file='%s.txt' % calc3
 target = open(file)
 aaaaa=[]
 aaaaa=file.split('.')
 #print aaaaa[0]
 calc3=calc3+1
 
 a=[]
 for line in target.readlines():
   hehe = line
   hehe_a=tsplit(hehe, (':', ';'))    
   a.append(hehe_a[1:2].pop())        #去掉列表中的列表
    
 #print a                              一行为单位的列表
 
 sep=''
 aaa=sep.join(a)
 saigo=aaa.split(' ')
 saigo.remove('')
 
 sum_sapce = 0
 for i in saigo:
   if i=='':
     sum_sapce+=1
 
 calc = 0
 while calc != sum_sapce:
   calc+=1                              #去掉全部空格
   saigo.remove('')
                           
 
 sum_list=0
 for line in saigo:                   #记录有多少列表
   sum_list+=1
 
 time=[]
 calc2=0
 while(calc2<=11):
   time.append(chr(int(saigo[calc2],16)))
   calc2+=1
   
 date=time[0]+time[1]                  #记录时间
 hour=time[2]+time[3]
 minute=time[4]+time[5]
 second=time[6]+time[7]
 year=time[8]+time[9]
 month=time[10]+time[11]
 
 flag=0                               #记录是否为超过了列表的总数
 pre=12
 next=18
 brethe=[]                                           #分别为记录各体征的列表
 heart=[]
 bodymoving=[]
 stop=[]
 keep=[]
 while (flag <sum_list and pre<sum_list-6): 
   t=pre
   if(saigo[pre]=='FF'):
     pass
   else:
     brethe.append(int(saigo[t+1],16))                #转换十进制
 	
     heart.append(int(saigo[t+2],16))
 	
     bodymoving.append(int(saigo[t+3],16))
 	
     stop.append(int(saigo[t+4],16))
 	
     keep.append(int(saigo[t+5],16))
   pre+=6
   flag+=1
   
 print "date is %s" % date
 print "hour is %s" % hour
 print "minute is %s" % minute
 print "second is %s" % second
 print "year is %s" % year
 print "month is %s" % month
 #print "brethe is %s" % brethe                          #这些是输出整个所有的数据
 #print "heart is %s" % heart
 #print "bodymoving is %s" % bodymoving
 #print "stop is %s" % stop
 #print "keep is %s" % keep                           
 print "brethe is %s" % (sum(brethe)/len(brethe))
 print "heart is %s" % (sum(heart)/len(heart))
 print "bodymoving is %s" % (sum(bodymoving)/len(bodymoving))
 print "stop is %s" % (sum(stop)/len(stop))
 print "keep is %s" % (sum(brethe)/len(brethe))
 
 
 aaaaaa='20'+str(year)+'-'+str(month)+'-'+str(date)
 bbbbbb='%s' % aaaaaa
 cccccc="'%s'" % bbbbbb
 #print cccccc
 
 import MySQLdb                                                 #存入mysql
 
 conn= MySQLdb.connect(
         host='localhost',
         port = 3306,
         user='root',
         passwd='',
         db ='mySleep',
         )
 cur = conn.cursor()
 
 cur.execute("create table data_%s (data varchar(20), hour varchar(20),minute varchar(20),second varchar(20),year varchar(20),month varchar(30),brethe varchar(20),heart varchar(20),bodymoving varchar(20),stop varchar(20),keep varchar(20),date date)" % (aaaaa[0]))
 
 cur.execute("insert into data_%s values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" % (aaaaa[0],date,hour,minute,second,year,month,sum(brethe)/len(brethe),sum(heart)/len(heart),sum(bodymoving)/len(bodymoving),sum(stop)/len(stop),sum(brethe)/len(brethe),cccccc))
 
 cur.close()
 conn.commit()
 conn.close()
 
 #print aaaaaa

