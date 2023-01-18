from art import *
import os, queue

q = queue.Queue()

class Setup:
    def __init__(self) -> None:
        self.accounts = []
        self.number_acc = 0
    
    def generate_title(self,name):
        
        """retruns an ascii title for your checkers using the art library

        Args:
            name (str): name of your checker

        Returns:
            str: checker name in ASCII (big gaming)
        """
        print(text2art(name))

    def windowname(self,title):
        """change the window name of the checker, using the OS module

        Args:
            title (str): the text you wanna put in
        """
        os.system(f'title {title}')


    def load_combos(self):

        with open('combo.txt','r') as combo:
            for line in combo:
                q.put(line.strip())
                self.accounts.append(line.strip())
                self.number_acc += 1

        print(f'> loaded {self.number_acc} acc')

        



