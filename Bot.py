"""TIKTOK BOT FILE"""

# ! Tiktok Bot

# NOTE : IMPORT LIBRARY
import time
from colorama import Fore, init
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from os import system, get_terminal_size

init()
system("mode 800")
system("title Tiktok Bot -By rifqanzalbina")

# * Def Color
def color(str, color):
    if color.lower() == "green":
        result = f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}{str}{Fore.WHITE}]{Fore.LIGHTGREEN_EX}"
    
    elif color.lower() == "red":
        result = f"{Fore.WHITE}[{Fore.LIGHTRED_EX}{str}{Fore.WHITE}]{Fore.LIGHTRED_EX}"

    return result

# * Def Align
def align(str):
    lines = str.splitlines()
    greatest = []
    for i in lines:
        greatest.append(len(i))
        
    for i in lines:
        length = round(int(greatest[-1]/2))
        print(f"{' '*round(get_terminal_size().columns/2-length)}{i}")

class printing():
    
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        
    def text():
        text = f"""{Fore.LIGHTMAGENTA_EX}
         _____  _  _     _           _      ____          _   
\t\t\t\t|_   _|(_)| | __| |_   ___  | | __ | __ )   ___  | |_ 
\t\t\t\t  | |  | || |/ /| __| / _ \ | |/ / |  _ \  / _ \ | __|
\t\t\t\t  | |  | ||   < | |_ | (_) ||   <  | |_) || (_) || |_ 
\t\t\t\t  |_|  |_||_|\_\ \__| \___/ |_|\_\ |____/  \___/  \__| By @rifqanzalbina
        """
        text = text.replace('▪', f'{Fore.GREEN}▪{Fore.LIGHTMAGENTA_EX}')
        text = text.replace('•', f'{Fore.GREEN}•{Fore.LIGHTMAGENTA_EX}')
        text = text.replace('·', f'{Fore.GREEN}·{Fore.LIGHTMAGENTA_EX}')
        text = text.replace('.', f'{Fore.GREEN}.{Fore.LIGHTMAGENTA_EX}')
        align(text)

    def info():
        align(f"""{Fore.WHITE}
           {color(">", "green")} About: {Fore.LIGHTMAGENTA_EX}This Tool Uses Zefoy To Bot TikTok Stats.{Fore.WHITE}                     ║
           {color(">", "green")} Updates: {Fore.LIGHTMAGENTA_EX}Error Fix & Adjustment --9/15/2022{Fore.WHITE}                          ║
           {color(">", "green")} Made By: {Fore.LIGHTMAGENTA_EX}rifqanzalbina{Fore.WHITE}                                                ║
           {color(">", "green")} Github: {Fore.LIGHTMAGENTA_EX}https://github.com/rifqanzalbina/{Fore.WHITE}                             ║
           {color(">", "green")} Download Chrome Driver: {Fore.LIGHTMAGENTA_EX}https://chromedriver.chromium.org/downloads{Fore.WHITE}  ║       
""")
        
    def options():
        align(f"""{Fore.WHITE}
           {color("1", "green")} {Fore.LIGHTMAGENTA_EX}Start{Fore.WHITE}            
           {color("2", "green")} {Fore.LIGHTMAGENTA_EX}Info{Fore.WHITE}             
           {color("3", "green")} {Fore.LIGHTMAGENTA_EX}Options{Fore.WHITE}         
           {color("4", "green")} {Fore.LIGHTMAGENTA_EX}Clear{Fore.WHITE}            
           {color("5", "green")} {Fore.LIGHTMAGENTA_EX}Exit{Fore.WHITE}                 
""")
        
    def botOptions():
        align(f"""{Fore.WHITE}
           {color("1", "green")} {Fore.LIGHTMAGENTA_EX}Follows{Fore.WHITE}          
           {color("2", "green")} {Fore.LIGHTMAGENTA_EX}Hearts{Fore.WHITE}           
           {color("3", "green")} {Fore.LIGHTMAGENTA_EX}Views{Fore.WHITE}            
           {color("4", "green")} {Fore.LIGHTMAGENTA_EX}Shares{Fore.WHITE}           
           {color("5", "green")} {Fore.LIGHTMAGENTA_EX}All{Fore.WHITE}                 
 """)
        
    def cooldowns(self):
        align(f"""{Fore.WHITE}
           {color(">", "green")} {Fore.LIGHTMAGENTA_EX}Cool Downs {color("<", "green")}║
           {color(">", "green")} {Fore.LIGHTMAGENTA_EX}Follows: {Fore.LIGHTCYAN_EX}{self.a}s{Fore.WHITE}             
           {color(">", "green")} {Fore.LIGHTMAGENTA_EX}Hearts: {Fore.LIGHTCYAN_EX}{self.b}s{Fore.WHITE}              
           {color(">", "green")} {Fore.LIGHTMAGENTA_EX}Views: {Fore.LIGHTCYAN_EX}{self.c}s{Fore.WHITE}               
           {color(">", "green")} {Fore.LIGHTMAGENTA_EX}Shares: {Fore.LIGHTCYAN_EX}{self.d}s{Fore.WHITE}                 
""")
        
    def refresh():
        system("cls")
        printing.text()
        align(f"\n\n\t\t\t{color('>', 'green')} Made By: {Fore.LIGHTMAGENTA_EX}Dreamer#5114 {color('<', 'green')}")
        align(f"\t\t\t\t{color('>', 'green')} {Fore.LIGHTGREEN_EX}Github: {Fore.LIGHTMAGENTA_EX}https://github.com/Setiawan007/TikTokBot {color('<', 'green')}")
        printing.options()


              
