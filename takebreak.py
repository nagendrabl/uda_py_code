import webbrowser
import time

loop=0
total_breaks = 3;
while loop != total_breaks:
  print ("printing for the time and it started at " + time.ctime())
  time.sleep(10)
  loop = loop+1
  webbrowser.open("www.google.com")  
  
print ("Iam out of the loop")

  
