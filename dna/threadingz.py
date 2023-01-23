import threading

class Threadingz:
    
    def __init__(self) -> None:
        """init of our class
        """
        
        self.threads = [] #initliazing the thread list
    
    def system(self,number_of_worker,target_worker,arg_thread):
            """System is just a simple thread system implementation. do not forget the args !!

            Args:
                number_of_worker (int): Number of threads / workers you want.
                target_worker (func name): the function name, this is what your worker is going to work on with
                arg_thread (arg): what item does the worker is going to work with
            """
        
            for self.i in range(number_of_worker): #for the number of worker
                
                self.t = threading.Thread(target=target_worker,args=(arg_thread,)) #t (thread) = one thread workig on the task using the argument from user
                
                self.threads.append(self.t) #we add t to the thread list
                
                self.t.start() #we start it
            
            
