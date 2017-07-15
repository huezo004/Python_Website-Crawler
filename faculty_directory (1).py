import requests 
import re 


page= requests.get('http://www.cs.fsu.edu/department/faculty/')

links=re.compile(r'http://www.cs.fsu.edu/department/faculty/[a-z]+/')

listLinks=links.findall(page.text) 

newlist=[]
for i in listLinks:
  if i not in newlist: 
      newlist.append(i)

for ele in newlist:

 tel=requests.get(ele)

 n=re.compile('(\(\d\d\d\))(\s)?(\d\d\d)([\s|-])(\d\d\d\d)') 

 snumber=n.search(tel.text)

 if snumber==None:
   tnum="N/A"
 else:
  tnum=snumber.group(1)+" "+snumber.group(3)+snumber.group(4)+snumber.group(5)


 email=re.compile('([a-z]+)\s\[')
 semail=email.search(tel.text) 

 if semail==None:
   ssemail="N/A"
 else:
   ssemail=semail.group(1) + " "+"[ at cs dot fsu dot edu]"

 o=re.compile("([\d]+[\w]?)(\s)(LOV|MCH|Love Building|LON|Love)")
 soffice=o.search(tel.text)

 if soffice==None:
  ssoffice="N/A"
 else: 
  ssoffice=soffice.group(1) + " " + soffice.group(3)

 name=re.compile('([\w]+)\s([\w]+)\s\|\s')
 sname=name.search(tel.text) 

 if sname==None:
   tname="N/A" 
 else: 
   tname=sname.group(1) +" "+sname.group(2)

 print "Name:" + " "+tname
 print "Office:" + " "+ ssoffice
 print "Telephone:" + " "+ tnum 
 print "E-mail" + " " + ssemail
 print "*******************************************"






