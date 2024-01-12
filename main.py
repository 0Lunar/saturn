import wget as w
import os
import requests as r
from bs4 import BeautifulSoup as bs
import sys
from colorama import Fore

def clean():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def banner():
    print(Fore.CYAN + '''
  _________       __                       
 /   _____/____ _/  |_ __ _________  ____  
 \\_____  \\\\__  \\\\   __\\  |  \\_  __ \\/    \\ 
 /        \\/ __ \\|  | |  |  /|  | \\/   |  \\
/_______  (____  /__| |____/ |__|  |___|  /
        \\/     \\/                       \\/ 
''')

def download(url):
    print(Fore.YELLOW + "\n Downloading the video..." + Fore.RESET)
    filename = w.download(url)
    os.rename(("./" + filename), ("./downloads/" + filename))
    print(Fore.GREEN + "\n\n Download finished for: " + filename + Fore.RESET)

def finDownloadURL(url):
    soup = bs(r.get(url).text, 'html.parser')
    for link in soup.find_all('source'):
        link = link.get('src')
    download(link)

def downloadFile(file):
    line = file.readline()
    while line != "":
        finDownloadURL(line)

def checkfolder():
    if os.path.isdir("./downloads") == False:
        os.mkdir("./downloads")

def menu():
    print(Fore.CYAN + "\n 1. download video")
    print(" 2. download more videos from a file")
    print(" 3. exit" + Fore.RESET)

if __name__ == "__main__":
    try:
        banner()
        menu()
        choise = int(input(Fore.GREEN + "\n => "))
        if choise == 1:
            url = input(Fore.YELLOW + "\n Enter the animesaturn url: ")
            checkfolder()
            finDownloadURL(url)
        elif choise == 2:
            file = input(Fore.YELLOW + "\n Enter the file path: ")
            file = open(file, "r")
            checkfolder()
            downloadFile(file)
        else:
            print("\n Error")
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n KeyboardInterrupt detected, exiting..." + Fore.RESET)
        sys.exit()
    except r.exceptions.MissingSchema:
        print(Fore.YELLOW + "\n Error, invalid url" + Fore.RESET)
    except r.exceptions.ConnectionError:
        try:
            r.get("https://www.google.com")
            print(Fore.YELLOW + "\n Invalid url" + Fore.RESET)
        except:
            print(Fore.YELLOW + "\n Connection error" + Fore.RESET)
    #except:
    #    print(Fore.RED + "\n Unexpected error" + Fore.RESET)
