

# import socket               # Import socket module

# s = socket.socket()         # Create a socket object
# host = socket.gethostname() # Get local machine name
# port = 12345                # Reserve a port for your service.
# s.bind((host, port))        # Bind to the port

# s.listen(5)                 # Now wait for client connection.
# while True:
#    c, addr = s.accept()     # Establish connection with client.
#    print 'Got connection from', addr
#    c.send('Thank you for connecting')
#    c.close() 




#pip install requests
#pip install beautifulsoup4 

# from bs4 import BeautifulSoup

# import requests

# url = raw_input("Enter a website to extract the URL's from: ")

# r  = requests.get("http://" +url)

# data = r.text

# soup = BeautifulSoup(data)

# for link in soup.find_all('a'):
#     print(link.get('href'))