import os

def menu():

    print(""" 
__          _______ _   _______          _     
\ \        / / ____| | |__   __|        | |    
 \ \  /\  / / (___ | |    | | ___   ___ | |___ 
  \ \/  \/ / \___ \| |    | |/ _ \ / _ \| / __|
   \  /\  /  ____) | |____| | (_) | (_) | \__ /
    \/  \/  |_____/|______|_|\___/ \___/|_|___/
========================================
Created By AnonHacker
Channel: youtube.com/kalinuxx
Facebook: facebook.com/kalinuxtutorialss
Ver: 1.0
========================================
00. Install ALL.
------------------------------------------
1. Install Metasploit 
2. Install Social-Engineer Toolkit (SET)
3. Install Nmap
4. Install SqlMap
------------------------------------------
99. Exit
========================================
""")

loop = True

while loop:
    menu()
    what = input("#: ")
    if what == "00":
        print("================================")
        print("This will install: Metasploit, SET, Nmap, SQLMap.")
        print("----------------")
        hm = input("[?] Do you want to continue? (y/n): ")
        print("================================")
        if hm == "y":
            print("========================================================")
            print("[+] Installing all tools.")
            print(" this will take a long time.")
            print("========================================================")
            os.system("sudo apt-get install metasploit-framework postgresql")
            os.system("git clone https://github.com/trustedsec/social-engineer-toolkit/ set/")
            os.system("cd set")
            os.system("sudo apt-get install python")
            os.system("python3 setup.py install")
            os.system("sudo apt-get install nmap")
            os.system("sudo apt-get install sqlmap")
        else:
            rmenu = input("[?] Back to Menu? (y/n): ")
            if rmenu == "y":
                menu()
            else:
                break
    if what == "1":
        os.system("sudo apt-get install metasploit-framework postgresql")
        print("====================================")
        print("[+] metasploit installed successfully :)")
        print("[+] Type 'msfconsole' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "2":
        os.system("git clone https://github.com/trustedsec/social-engineer-toolkit/ set/")
        os.system("cd set")
        os.system("sudo apt-get install python")
        os.system("python3 setup.py install")
        print("====================================")
        print("[+] SET installed successfully :)")
        print("[+] Type 'setoolkit' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "3":
        os.system("sudo apt-get install nmap")
        print("====================================")
        print("[+] Nmap installed successfully :)")
        print("[+] Type 'Nmap' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "4":
        os.system("sudo apt-get install sqlmap")
        print("====================================")
        print("[+] SQLMap installed successfully :)")
        print("[+] Type 'SQLMap' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "99":
        print("Bye.")
        break