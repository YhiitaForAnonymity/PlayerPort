import socket
import pyfiglet
import colorama
import os
from colorama import *
import requests
import dns.resolver



def banner(): #github.com/YhiitaForAnonymity
    text = pyfiglet.figlet_format(text="PlayerPort",
    font="slant")
    os.system("cls") 
    print(Fore.BLUE + """  
    """)
    print(text)

def loop(): 
    print(Fore.BLUE + """""")
    service = input("»»»      Choose Service: ")

    if service == "1":
        complete()

    if service == "2":
        gaming()        

    if service == "3":
        server()   

def addon_1():
    with open(url + ".txt", "a") as file:
        result = dns.resolver.resolve(url, 'MX')
        for val in result:
            file.write('MX Record: ' + val.to_text() + '\n')
        
        result = dns.resolver.resolve(url, 'TXT')
        for val in result:
            file.write('TXT Record: ' + val.to_text() + '\n')
        
        result = dns.resolver.resolve(url, 'SOA')
        for val in result:
            file.write('SOA Record: ' + val.to_text() + '\n')
        
        result = dns.resolver.resolve(url, 'AAAA')
        for ipval in result:
            file.write('AAAA Record: ' + ipval.to_text() + '\n')
    
def complete():
    ports = [  1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 18, 19, 20, 21, 22, 23, 25, 27, 28, 29, 31, 33, 37, 38, 39, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 58, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 76, 78, 79, 80, 81, 82, 83, 84, 85, 86, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 101, 102, 104, 105, 106, 107, 108, 109, 110, 111, 113, 115, 117, 118, 119, 123, 126, 135, 137, 138, 139, 143, 151, 152, 153, 156, 158, 161, 162, 165, 169, 170, 177, 179, 180, 194, 199, 201, 209, 210, 213, 218, 220, 225, 226, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 259, 262, 264, 280, 300, 308, 311, 312, 318, 319, 320, 350, 351, 356, 366, 369, 370, 371, 376, 383, 384, 387, 388, 389, 399, 401, 427, 433, 434, 443, 444, 445, 464, 465, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 497, 498, 499, 500, 502, 504, 510, 512, 513, 514, 515, 517, 518, 520, 521, 523, 524, 525, 526, 530, 532, 533, 540, 542, 543, 544, 545, 546, 547, 548, 550, 554, 556, 560, 561, 563, 564, 565, 570, 571, 572, 573, 586, 587, 591, 593, 601, 604, 623, 624, 625, 626, 627, 628, 829, 830, 831, 832, 833, 843, 847, 848, 853, 860, 861, 862, 873, 888, 889, 890, 900, 901, 902, 903, 953, 981, 987, 989, 990, 991, 992, 993, 994, 995, 1010, 6672]
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1) 
        result = sock.connect_ex((ip_address, port))
        if result == 0:
            open_ports.append(port)
        sock.close()

    results = "\n".join(f"Port {port}: Open" for port in open_ports)

    with open(url + ".txt", "w") as file:
        file.write("Service: Complete " + "\n")
        file.write("IP: " + ip_address + "\n")
        for key, value in location_data.items():
            file.write(key + ": " + str(value) + "\n")
        file.write("Open Ports:" + "\n")
        file.write(results + "\n")
        addon_1()

def gaming():
    ports = [6672, 433, 3074, 5222, 3478, 3479, 5060, 5062, 5222, 6250, 500, 3544, 4500, 6667, 12400, 28910, 29900, 29901, 29920, 3569, 8080, 9946, 9988, 42124, 27015, 27036, 1119, 3724, 6012, 25565, 27015, 27036, 2099, 5222, 5223, 8088, 8393, 8400, 8446] 
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1) 
        result = sock.connect_ex((ip_address, port))
        if result == 0:
            open_ports.append(port)
        sock.close()

    results = "\n".join(f"Port {port}: Open" for port in open_ports)

    with open(url + ".txt", "w") as file:
        file.write("Service: Gaming " + "\n")
        file.write("IP: " + ip_address + "\n")
        for key, value in location_data.items():
            file.write(key + ": " + str(value) + "\n")
        file.write("Open Ports:" + "\n")
        file.write(results + "\n")
        addon_1()

def server():
    ports = [20, 21, 22, 25, 53, 80, 123, 179, 443, 445, 993, 135, 995, 9929, 445, 135, 137, 3343, 67, 2535, 389, 6600,	3343, 1801, 110, 563, 119, 31337, 3389]
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1) 
        result = sock.connect_ex((ip_address, port))
        if result == 0:
            open_ports.append(port)
        sock.close()

    results = "\n".join(f"Port {port}: Open" for port in open_ports)

    with open(url + ".txt", "w") as file:
        file.write("Service: Server " + "\n")
        file.write("IP: " + ip_address + "\n")
        for key, value in location_data.items():
            file.write(key + ": " + str(value) + "\n")
        file.write("Open Ports:" + "\n")
        file.write(results + "\n")
        addon_1()

banner() 
print(Fore.RED + """     
»»»»»»»»»»»»»»»»»»   Tos   »»»»»»»»»»»»»»»»»»  


»»»      Use this tool only for educational purposes only
»»»      Author won't be responsible for any misuse of this tool
""")
print(Fore.BLUE + """""")
print(Fore.MAGENTA + """
»»»»»»»»»»»»»»»»»» Website »»»»»»»»»»»»»»»»»»
""")
url = input("»»»      Website/Ip: ")
ip_adress = url
ip_address = socket.gethostbyname(url)
response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()

location_data = {
    "City": response.get("city"),
    "Region": response.get("region"),
    "Country": response.get("country_name"),
    "Provider": response.get("org"),
    "Currency": response.get("timezone"), 
    "Phonenumber": response.get("country_calling_code"), 
    "Timezone": response.get("timezone"), 
}

latitude = response.get("latitude")
global lat
lat = str(latitude)
longitude = response.get("longitude")
global long
long = str(longitude)

url1 = "https://google.com/maps/place/" + lat +  "," + long + "/@" + lat + "," + long + ",16z"

print ("\n")
print(Fore.GREEN + """""")
print ("»»»»»»»»»»»»»»»»»» Services »»»»»»»»»»»»»»»»»»" + "\n")
print ("»    Complete  [1]" + "  Scan the most common ports" + "\n")
print ("»    Gaming    [2]" + "  Scan the most gaming ports" + "\n")
print ("»    Server    [3]" + "  Scan the most server ports" +"\n")

loop()