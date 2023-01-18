from art import *
import os

class Setup:
    def __init__(self):
        pass
    
    def generate_title(name):
        """retruns an ascii title for your checkers using the art library

        Args:
            name (str): name of your checker

        Returns:
            str: checker name in ASCII (big gaming)
        """
        return text2art(name)

    def windowname(title):
        """change the window name of the checker, using the OS module

        Args:
            title (str): the text you wanna put in
        """
        os.system(f'title {title}')



