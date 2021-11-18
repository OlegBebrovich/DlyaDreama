import os
from menu_config import menu
try:
    import aminofix
except ModuleNotFoundError:
    os.system("pip install amino.fix")
    import aminofix
try:
    from tabulate import tabulate
except ModuleNotFoundError:
    os.system("pip install tabulate")
    from tabulate import tabulate
try:
    import pyfiglet
except ModuleNotFoundError:
    os.system("pip install pyfiglet")
    import pyfiglet
try:
    from colorama import init, Fore
except ModuleNotFoundError:
    os.system("pip install colorama")
    from colorama import init, Fore
    init()

print(Fore.LIGHTGREEN_EX)

def login():
    try:
        client.login(email=input("Enter email: "), password=input("Enter password: "))
        print("Bot login in account")
    except Exception:
        print("Failed login. Relogin")
        login()

def com_steal():
    link = input("Enter object link: ")
    comId = client.get_from_code(link).comId
    com_steal = client.get_community_info(comId=comId)
    print(f"\nCommunity title: {com_steal.name}", f"Community icon(url): {com_steal.icon}", f"Community theme color: {com_steal.themeColor}", f"Community prom.medialist(url): {com_steal.promotionalMediaList}", f"Community theme left side panel: {com_steal.themeLeftSidePanelColor}", sep="\n")
    print("Community medialist: ")
    for media in com_steal.mediaList:
        print(media)

def user_steal():
    link = input("Enter user link: ")
    choose = input(f"Is global?(y/n)\nChoose: ")
    if choose == "y":
        userId = client.get_from_code(link).objectId
        user_steal = client.get_user_info(userId=userId)
        print(f"User nickname: {user_steal.nickname}", f"User icon(url): {user_steal.icon}", f"User aminoId: {user_steal.aminoId}", sep="\n")
    elif choose == "n":
        userId = client.get_from_code(link).objectId
        comId = client.get_from_code(link).comId
        sub_client = aminofix.SubClient(comId=comId, profile=client.profile)
        user_steal = sub_client.get_user_info(userId=userId)
        print(f"User nickname: {user_steal.nickname}", f"User icon(url): {user_steal.icon}", f"User background or back.color: {user_steal.backgroundImage} or {user_steal.backgroundColor}", f"User medialist: \n",  sep="\n")
        for media in user_steal.mediaList:
            print(media)

client = aminofix.Client()
logo = pyfiglet.figlet_format(text="Steal Manager", font="chunky")
print(logo, "Created by celt", "Telegram: @celt_is_god\n", sep="\n")
login()
print(tabulate(menu.main_menu, tablefmt="fancy_grid"))
choose = input("Choose your action: ")
if choose == "1":
    com_steal()
elif choose == "2":
    user_steal()