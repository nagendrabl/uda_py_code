import io
import urllib.request


def checkprofanity(datatocheck):
    googleurl="http://www.wdyl.com/profanity?q="+urllib.parse.quote_plus(datatocheck)
    print(googleurl)
    try:
        openhandle = urllib.request.urlopen(googleurl)
        returndata = openhandle.read().decode("utf8", 'ignore')
        openhandle.close()
    except urllib.error.URLError as e: returndata = "Exception handled."
    if "true" in returndata:
       print("Profanity present")
    elif "false" in returndata:
       print ("No profanity present")
    else:
       print("Exception when parsing the files") 
                 
    


def read_file():
    openedfile=open(r'C:\Users\nagendra\Desktop\win\movie_quotes.txt',mode='r',encoding="ascii")
    data= openedfile.read()
    openedfile.close()
    checkprofanity(data)


read_file()

