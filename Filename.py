import os
import string
def rename_files():
    file_list = os.listdir(r"C:\Users\nagendra\Dropbox\Udacity\Full Stack Developer\python\prank")
    print (file_list)
    os.chdir(r"C:\Users\nagendra\Dropbox\Udacity\Full Stack Developer\python\prank")
    for file_name in file_list:
        os.rename(file_name,file_name.translate({ord('0'):None, ord('1'):None, ord('2'):None, ord('3'):None,ord('4'):None,ord('5'):None,ord('6'):None,ord('7'):None,ord('8'):None,ord('9'):None}))



rename_files()
                    
