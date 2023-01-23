from art import * #ascii name generator. use pip to install
import queue,time,fade,os
from threading import Lock

lock = Lock()

class DNA:
    
    def __init__(self) -> None:
        """init of our class
        """
        
        self.queue = queue.Queue() #initializing the FIFO queue
        
        self.proxylist = [] #proxylist storage
            
    
    def generate_title(self,name):
        """retruns an ascii title for your checkers using the art library

        Args:
            name (str): name of your checker

        Returns:
            str: checker name in ASCII (big gaming)
        """
        print(fade.purpleblue(text2art(name,'cricket')))

    def load_combos(self):
        """Loads the combo from users and add account to the queue
        """

        with open('combo.txt','r') as combo:
            for line in combo:
                try:
                    self.queue.put(line.strip())
                except:
                    pass

        print(f'> loaded {self.queue.qsize()} accounts')
        
    def load_proxylist(self):
        """Same as combos, except it loads the proxies and paste it in the self.proxies list
        """
        
        with open('proxies.txt','r') as pl:
            for line in pl:
                try:
                    self.proxylist.append(line.strip)
                except:
                    pass
                
        print(f'> loaded {len(self.proxylist)} proxies')
        
    def cpm_calculation(self):
        """Thanks sat for the help <3 cracked.io/Sat
        """
        while True:
            self.CpmBuilder = 0 #we init the cpm at 0
            time.sleep(1) #wait one sec to check how much checks we did
            self.CpmFinal = self.CpmBuilder #we asign the value
            self.CpmFinal *= 60 #and multiply it to 60 for a whole minute, see da trick ?
            
            
    def output(self,paste):
        if not os.path.exists('Results'): #if no directory results
            os.mkdir('Results') #create one
            with open('Results\Hits.txt','w+') as file: #write in this file, if no file, create one

                file.writelines(f'{paste}\n') #paste te account and jump to next line

                
        else: #if results directory exists
            with open('Results\Hits.txt','a+') as file: #open the file 
                file.writelines(f'{paste}\n') #append account at the end

        


