from phone import Phonenumber
from socket import gethostname
import sqlbash
import pywhatkit
import webbrowser
import os

while True:
    print(f"root@{gethostname()}:/c/ (master)")
    cmd = input("> ")
    if cmd == "phone":
        n = input(": ")
        number = Phonenumber(n)
        if not number.isValid():
            print("Invalid Number!")
            ...
        print(number.base())
        print(number.tz()[0])
        print(f'{number.carrier()[0]}\n{number.carrier()[1]}')

    elif cmd == "sqlbash":
        sqlbash.mainloop("sql@sql-bash.127.0.0.1:5000")

    elif cmd == "whatsapp":
        number = input("Phone Number: ")
        strftime = input("Time to send (Format:hh:mm)\n:")
        mesg = input("Message: ")
        webbrowser.open("web.whatsapp.com")
        pywhatkit.sendwhatmsg(number,mesg,strftime.split(":")[0],strftime.split(":")[1])
        