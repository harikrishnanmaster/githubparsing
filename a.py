import requests
from bs4 import BeautifulSoup
import re
import csv
import re
project = raw_input("enter project name")
for i in range(1,6):
 
 
 
 url = "https://github.com/search?p=%s&q=%s&type=Repositories"%(i,project)
  
 r = requests.get(url)

 soup = BeautifulSoup(r.content,"html.parser")

 li = soup.find_all("div", {"class": "repo-list-item d-flex flex-justify-start py-4 public source"})
 for l in li:
   print "--------------------------------------------------------------------------------------------------------------"
   try:
     
     
     print "url:https://github.com%s"%(l.find('a').get('href'))
   except:
     pass
  
   try:
     print "description: %s"%(l.find("p",{"class":"col-9 d-inline-block text-gray mb-2 pr-4"}).get_text())
   except:
     pass
   try:  
     print "labels%s"%(l.find("div",{"class":"topics-row-container col-9 d-inline-flex flex-wrap flex-items-center f6 my-1"}).get_text())
     
   except:
     pass
   try:  
     print "language:%s" %(l.find("div",{"class":"d-table-cell col-2 text-gray pt-2"}).get_text())
   except:
     pass
   
   try:  
     print "averagestars:%s"%(l.find("a",{"class":"muted-link"}).get_text())
   except:
     pass
     
  #links = l.find_all("a", {"class": "v-align-middle"})
  #for link in links:
    
   
      
      #a = "https://github.com%s" %(link.get("href"))
   
      
      #print a
      
  
    