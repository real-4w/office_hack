import socket    
from requests import get

hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)    
print(f"Your Computer Name is: {hostname}")    
print(f"Your local IP address is: {IPAddr}")  

ip = get('https://api.ipify.org').text
print (f"My public IP address is: {ip}")
