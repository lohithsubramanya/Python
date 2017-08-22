# import socket               # Import socket module

# s = socket.socket()         # Create a socket object
# host = socket.gethostname() # Get local machine name
# port = 12345                # Reserve a port for your service.

# s.connect((host, port))
# print s.recv(1024)
# s.close()  




# import threading

# class myThread (threading.Thread):
#     def __init__(self, threadID, name):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
        
#     def run(self):
#         print "Starting " + self.name
#         print_time(self.name)
#         print "Exiting " + self.name

#     def func(self):
#         print 'function 2'

# def print_time(threadName):
    
#     print 'this is inside func      ', threadName
#     for i in range(1,100):
#     	print i
        

# # Create new threads
# thread1 = myThread(1, "Thread-1")
# thread2 = myThread(2, "Thread-2")

# # Start new Threads
# thread1.start()
# thread2.start()



