class Proxy:
    def __init__(self) -> None:
        
        self.http = {
                    'http': 'http://',
                    'https': 'http://',
                    }
        
        self.socks4 = {
                    'socks4://': 'http://',
                    }
        
        self.socks5 = {
                    'socks5://': 'http://',
                    }  
