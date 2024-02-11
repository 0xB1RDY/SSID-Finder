# BANNER
from colorama import Fore, just_fix_windows_console
import os

just_fix_windows_console()
os.system("cls")

print(f"""
{Fore.WHITE} ███████ ███████ ██ ██████        {Fore.LIGHTRED_EX}███████ ██ ███    ██ ██████  ███████ ██████ {Fore.RESET} 
{Fore.WHITE} ██      ██      ██ ██   ██       {Fore.LIGHTRED_EX}██      ██ ████   ██ ██   ██ ██      ██   ██{Fore.RESET}
{Fore.WHITE} ███████ ███████ ██ ██   ██ █████ {Fore.LIGHTRED_EX}█████   ██ ██ ██  ██ ██   ██ █████   ██████ {Fore.RESET}
{Fore.WHITE}      ██      ██ ██ ██   ██       {Fore.LIGHTRED_EX}██      ██ ██  ██ ██ ██   ██ ██      ██   ██{Fore.RESET}  [ Ctrl + C to stop ]
{Fore.WHITE} ███████ ███████ ██ ██████        {Fore.LIGHTRED_EX}██      ██ ██   ████ ██████  ███████ ██   ██{Fore.RESET}  [ Created by Birdy ]""")
size = os.get_terminal_size()
print("━" * size.columns)

# MAIN PROGRAM
import subprocess
import time
import datetime

captured = set()

def get_networks():
    try:
        output = subprocess.check_output(["netsh", "wlan", "show", "networks", "mode=bssid"], encoding="utf-8")
        lines = output.split("\n")
        ssid = None
        bssid = None

        for line in lines:
            line = line.strip()
            if line.startswith("SSID"):
                ssid = line[9:].strip()
            elif line.startswith("BSSID"):
                bssid = line[25:].strip()
            if ssid and bssid:
                if (ssid, bssid) not in captured:
                    print(f"{Fore.LIGHTGREEN_EX}Found:{Fore.RESET} {ssid} -> {bssid}")
                    captured.add((ssid, bssid))
                    ssid = None
                    bssid = None
                else:
                    break

    except Exception as e:
        print(e)

while True:
    try:
        get_networks()
        time.sleep(0.5)
    except KeyboardInterrupt:
        print("━" * size.columns)
        write_to_file = input("Write SSID's and BSSID's to file? (Y/N): ")
        if write_to_file.startswith("y"):
            now = datetime.datetime.now()
            filename = "Results_{}-{}-{}-{}-{}.txt".format(now.day, now.month, now.year, now.hour, now.minute)
            try:
                with open(filename, "w+") as file:
                    file.writelines(str(captured))
                    break
            except Exception as e:
                print(e)
                break
        else:
            break