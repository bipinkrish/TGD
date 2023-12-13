from pyrogram import Client
from os.path import exists
from os import remove
from sys import stdout

configfile = "tgd.txt"

if not exists(configfile):
    api_id = input("\nAPI ID: ")
    api_hash = input("API HASH: ") 
    check = input("Do you have String Session? (y/n): ")
    if check.lower() == "y":
        ss = input("SESSION STRING: ")
    else:
        print()
        with Client("TGD", api_id=api_id, api_hash=api_hash, in_memory=True) as temp:
            ss = temp.export_session_string()
        print()
    with open(configfile,"w") as file:
        file.write(api_id + "\n" + api_hash + "\n" + ss)
else:
    with open(configfile, "r") as file:
        data = file.readlines()
    try:
        api_id, api_hash, ss = data
    except:
        remove(configfile)
        print("Retry...")
        exit(0)
        

acc = Client("myacc" ,api_id=api_id, api_hash=api_hash, session_string=ss)
try:
    with acc:
        me = acc.get_me()
        print("\nLogged in as:", me.id)
except:
    remove(configfile)
    print("\nMaybe Wrong Crenditals...")
    exit(0)
    
    
def progress(current, total, length=50):
    progress_percent = current * 100 / total
    completed = int(length * current / total)
    bar = f"[{'#' * completed}{' ' * (length - completed)}] {progress_percent:.1f}%"
    stdout.write(f"\r{bar}")
    stdout.flush()


print("""
Examples:

    https://t.me/xxxx/1423
    https://t.me/c/xxxx/10
    https://t.me/xxxx/1001-1010
    https://t.me/c/xxxx/101 - 120\n\n""")

link = input("Enter the link: ")
print()


if link.startswith("https://t.me/"):
    datas = link.split("/")
    temp = datas[-1].replace("?single","").split("-")
    fromID = int(temp[0].strip())
    try: toID = int(temp[1].strip())
    except: toID = fromID

    if link.startswith("https://t.me/c/"):
        chatid = int("-100" + datas[4])
    else:
        chatid = datas[3]

else:
    print("Not a Telegram Link")
    exit(0)

with acc:
    total = toID+1 - fromID
    for msgid in range(fromID, toID+1):
        msg = acc.get_messages(chatid, msgid)
        
        print("Downloding:", msgid, f"({(msgid - fromID + 1)}/{total})")
        try:
            file = acc.download_media(msg, progress=progress)
            print("\nSaved at", file, "\n")
        except ValueError as e:
            print(e, "\n")
            
input("Press enter to exit...")
