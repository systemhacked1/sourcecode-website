
import  requests
import pyfiglet
import os
from time import sleep
print('\033[1;3mDo you want Souce code any Web Site ?')
print('Wait .. Iam here to help You ! ')
sleep(3)
def banner():
        os.system('clear')
        sleep(2)
        ban=pyfiglet.figlet_format('No System is Safe ')
        print(ban )
banner()

def source():
        url=str(input('Enter a URL :> '))
        print(' Loading .. ')
        print('\033[30m Remember You should Follow me in Telegram $_$')
        sleep(3)
        print('''
        ********************
        https://t.me/System_Hac
        ********************
        ''')
        sleep(5)

        os.system('clear')
        res =requests.get(url)
        #print(res)
        file_path =input('Enter a File Path : ')
        file =open(file_path ,  'w')
        file.write(res.text)
        file.close()
source()