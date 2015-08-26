import webbrowser
import time

loop=0
total_breaks = 3;
while loop != total_breaks:
  print ("printing for the time and it started at " + time.ctime())
  loop = loop+1
  time.sleep(10)

print ("Iam out of the loop")

  
