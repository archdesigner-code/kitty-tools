# │┤╣║╗╝┐└┴┬├─┼╚╔╩╦╠═╬┘┌

import requests, json, os, sys, time, webbrowser, discord
from colorama import Fore, init, Style
from discord.ext import commands
from requests import get

__version__ = "1.0"
init(autoreset=True)

class Macpyoui:
    def __init__(self, api):
        self.api = api

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

site = "https://api.macvendors.com/"
data = Macpyoui(site)
reset = Style.RESET_ALL
purple = Fore.MAGENTA

def mac_trace():
    clear()
    macaddress = input(f"{purple}MAC address: {reset}")
    macsend = data.api + macaddress
    vendorsearch = get(macsend).text
    if "Not Found" in vendorsearch:
        print("MAC address not found")
        time.sleep(2)
        mac_trace()
    elif len(sys.argv) == 1:
        print("No MAC address entered")
        time.sleep(2)
        mac_trace()
    else:
        print(vendorsearch)
        time.sleep(5)
        main()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def geolocater():
    clear()
    ip = input(f"{purple}IP{reset}: ")
    clear()
    api = f"https://ipinfo.io/{ip}/json"
    response = requests.get(api)
    data = response.json()
    print(f"{purple}IP: {reset}{data.get('ip')}")
    print(f"{purple}City: {reset}{data.get('city')}")
    print(f"{purple}Region: {reset}{data.get('region')}")
    print(f"{purple}Country: {reset}{data.get('country')}")
    print()
    input(f"{purple}Press anything to return..{reset}")
    main()

def webhook_info():
    try:
        clear()
        webhook = input(f"{purple}Webhook: {reset}")
        r = requests.get(webhook)

        if r.status_code == 200:
            data = r.json()

            print(f"{purple}Name: {reset}{data.get('name')}")
            print(f"{purple}ID: {reset}{data.get('id')}")
            print(f"{purple}Channel ID: {reset}{data.get('channel_id')}")
            print(f"{purple}Guild ID: {reset}{data.get('guild_id')}")
            print(f"{purple}Avatar: {reset}{data.get('avatar')}")
            print(f"{purple}Token: {reset}{data.get('token')}")
            print(f"{purple}Application ID: {reset}{data.get('application_id')}")
            print()
            input(f"{purple}Press anything to return..{reset}")
            main()
        else:
            clear()
            print(f"{purple}Failed{reset} to fetch webhook info. Status code: {r.status_code}")
            time.sleep(2)
            main()

    except requests.exceptions.RequestException as e:
        clear()
        print(f"{purple}Error:{reset} {e}")
        time.sleep(2)
        main()

def banner():
    print(f"{purple}                     ██╗  ██╗██╗████████╗████████╗██╗   ██╗  ████████╗ ██████╗  ██████╗ ██╗     ███████╗")
    print(f"{purple}                     ██║ ██╔╝██║╚══██╔══╝╚══██╔══╝╚██╗ ██╔╝  ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝")
    print(f"{purple}                     █████╔╝ ██║   ██║      ██║    ╚████╔╝█████╗██║   ██║   ██║██║   ██║██║     ███████╗")
    print(f"{purple}                     ██╔═██╗ ██║   ██║      ██║     ╚██╔╝ ╚════╝██║   ██║   ██║██║   ██║██║     ╚════██║")
    print(f"{purple}                     ██║  ██╗██║   ██║      ██║      ██║        ██║   ╚██████╔╝╚██████╔╝███████╗███████║")
    print(f"{purple}                     ╚═╝  ╚═╝╚═╝   ╚═╝      ╚═╝      ╚═╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝")
    print()

def ip_pinger():
    clear()
    ip = input(f"{purple}IP{reset}: ")
    clear()

    result = os.system(f"ping -n 4 {ip}")

    if result == 0:
        print(f"{purple}IP is online{reset}")
        time.sleep(3)
        main()
    else:
        print(f"{purple}IP is offline or unreachable{reset}")
        time.sleep(3)
        main()

def webhook_spam():
    clear()
    message = input(f"{purple}Message{reset}:")
    webhook = input(f"{purple}Webhook{reset}: ")
    user = input(f"{purple}Username{reset}: ")

    data = {
        "content": f"{message}",
        "username": f"{user}",
    }

    for i in range(100):
        requests.post(webhook, json=data)

    print(f"{purple}Finished!{reset}")
    time.sleep(2)
    main()

def raid():
    clear()
    print(f"{purple}Note{reset}: This is a work in progress, might break easily.")
    message = input(f"{purple}Message{reset}: ")
    token = input(f"{purple}Bot token{reset}: ")
    @bot.event
    async def on_ready():
        print(f"Run !raid to use.")
        print(f"Logged in as {bot.user}")

    @bot.command()
    async def raid(ctx):
        guild = ctx.guild

        for i in range(100):
            channel = await guild.create_text_channel("GOODBYE")
            await channel.send(f"{message} {i+1}")

        await bot.close()
        main()

    bot.run(token)

def webhook_delete():
    clear()
    webhook = input(f"{purple}Webhook{reset}: ")
    requests.delete(webhook)
    print(f"{purple}Finished{reset}!")
    time.sleep(2)
    main()

def main():
    while True:
        try:
            clear()
            banner()
            print()
            print(f"                    {purple}<<{reset}1{purple}>>{reset} {purple}[{reset}Webhook Information{purple}]                                    {purple}<<{reset}5{purple}>>{reset} {purple}[{reset}IP Geolocator{purple}]{reset}")
            print(f"                    {purple}<<{reset}2{purple}>>{reset} {purple}[{reset}Raid Discord server{purple}]                                    {purple}<<{reset}6{purple}>>{reset} {purple}[{reset}IP Pinger{purple}]{reset}")
            print(f"                    {purple}<<{reset}3{purple}>>{reset} {purple}[{reset}Webhook Deletetion{purple}]                                     {purple}<<{reset}7{purple}>>{reset} {purple}[{reset}Mac trace{purple}]{reset}")
            print(f"                    {purple}<<{reset}4{purple}>>{reset} {purple}[{reset}Webhook Spammer{purple}]                                        {purple}<<{reset}8{purple}>>{reset} {purple}[{reset}Credits{purple}]{reset}")
            print(f"                                                     {purple}<<{reset}q{purple}>>{reset} {purple}[{reset}Quit{purple}]")
            print()
            x = input(f"[{purple}>{reset}] Choice: ")
            if x == "1":
                webhook_info()
            elif x == "2":
                raid()
            elif x == "3":
                webhook_delete()
            elif x == "4":
                webhook_spam()
            elif x == "5":
                geolocater()
            elif x == "6":
                ip_pinger()
            elif x == "7":
                mac_trace()
            elif x == "8":
                print("decoy -- creator, coder, banner creator.")
                time.sleep(2)
                main()
            elif x == "q":
                sys.exit(0)
            else:
                print(f"{purple}Invalid{reset} option!")
                time.sleep(2)
                main()
        except Exception as E:
            print(f"{purple}Error{reset}: {E}")
            time.sleep(3)
            main()


if __name__ == '__main__':
    main()
