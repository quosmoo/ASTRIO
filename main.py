import requests, os, sys, subprocess, webbrowser
from pystyle import *
from time import sleep

os.system("mode 90,40 | title ")

banner = f'''
{" █████╗ ███████╗████████╗██████╗ ██╗ ██████╗ ".center(90)}
{"██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██║██╔═══██╗".center(90)}
{"███████║███████╗   ██║   ██████╔╝██║██║   ██║".center(90)}
{"██╔══██║╚════██║   ██║   ██╔══██╗██║██║   ██║".center(90)}
{"██║  ██║███████║   ██║   ██║  ██║██║╚██████╔╝".center(90)}
{"╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝ ╚═════╝ ".center(90)}
'''

menu_header = f'''
{"===  MENU  ===".center(90)}
'''
deleter_header = f'''
{"===  DELETE  ===".center(90)}
'''
spammer_header = f'''
{"===  SPAM  ===".center(90)}
'''
spamndelete_header = f'''
{"===  SPAM & DELETE  ===".center(90)}
'''

print(Colorate.Horizontal(Colors.blue_to_purple, banner, 1))
print(menu_header)

Write.Print("\n\n┌───[ASTRIO]-(Paste webhook)\n", Colors.blue_to_purple, interval=0.01)
url = Write.Input("└───>", Colors.blue_to_purple, interval=0.01, hide_cursor=False)


try:
    status = requests.get(url).status_code
except:
    subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])

if status == 200:
    Write.Print("Webhook found!\n\n", Colors.green, interval=0.025)
else:
    Write.Input("Webhook doesn't exist! Press ENTER go back.", Colors.blue_to_purple, interval=0.025)
    subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:]) 


Write.Print("1 | Spam\n", Colors.blue_to_purple, interval=0.025)
Write.Print("2 | Delete\n", Colors.blue_to_purple, interval=0.025)
menu = Write.Input("3 | Spam & Delete\n", Colors.blue_to_purple, interval=0.025, hide_cursor=False)

if menu == "1":
    try:
        os.system("cls")
    except:
        try:
            os.system("clear")
        except:
            for i in range(100):
                print("\n")

    print(Colorate.Horizontal(Colors.blue_to_purple, banner, 1))
    print(spamndelete_header)
    message = Write.Input("\nMessage=", Colors.blue_to_purple, interval=0.025, hide_cursor=False)
    longer_message = f"{message}\n" * 1000
    username = Write.Input("\nCustom Username=", Colors.blue_to_purple, interval=0.025, hide_cursor=False)
    data = {
        "username": username,
        "content": longer_message
    }
    errors = 0
    while errors < 10:
        for i in range(100):
            post = requests.post(url, data=data)
            sleep(0.1)
            if post.status_code == 400:
                errors += 1
                print(f"{post.status_code} | Error, webhook ratelimited")
            else:
                print(f"{post.status_code} | Sent")
            if errors == 10:
                requests.delete(url)
                Write.Input("Webhook automatically deleted after 10 errors\nENTER to go back\n", Colors.blue_to_purple, interval=0.025, hide_cursor=False)
                subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])

if menu == "2":
    try:
        os.system("cls")
    except:
        try:
            os.system("clear")
        except:
            for i in range(100):
                print("\n")

    print(Colorate.Horizontal(Colors.blue_to_purple, banner, 1))
    print(deleter_header)
    requests.delete(url)
    webbrowser.open(url)
    subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])

if menu == "3":
    try:
        os.system("cls")
    except:
        try:
            os.system("clear")
        except:
            for i in range(100):
                print("\n")

    print(Colorate.Horizontal(Colors.blue_to_purple, banner, 1))
    print(spamndelete_header)
    message = Write.Input("\nMessage=", Colors.blue_to_purple, interval=0.025, hide_cursor=False)
    longer_message = f"{message}\n" * 1000
    username = Write.Input("\nCustom Username=", Colors.blue_to_purple, interval=0.025, hide_cursor=False)
    data = {
        "username": username,
        "content": longer_message
    }
    errors = 0
    while errors < 10:
        for i in range(100):
            post = requests.post(url, data=data)
            sleep(0.1)
            if post.status_code == 400:
                errors += 1
                print(f"{post.status_code} | Error, webhook ratelimited")
            else:
                print(f"{post.status_code} | Sent")
            if errors == 10:
                requests.delete(url)
                Write.Input("Webhook automatically deleted after 10 errors\nENTER to go back\n", Colors.blue_to_purple, interval=0.025, hide_cursor=False)
                subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])


    requests.delete(url)
    webbrowser.open(url)
    subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
else:
    subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])