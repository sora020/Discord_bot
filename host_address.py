# IP address
 
# Importing socket library
import socket
 
# Function to display hostname and
# IP address
def get_Host_name_IP():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        print("--------\nHostname: {}\nIP: {}\n--------".format(host_name, host_ip))
    except:
        print("--------\nUnable to get Hostname and IP--------\n")

