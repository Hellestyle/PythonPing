from datetime import datetime
import os
import re
import ipaddress

def writeToFile(results):
    with open("pingresult.txt", "a+") as file:
        scanTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        stringResult= f"{'-'*24}\n|  Results for scan    |\n{'-'*24}\nTimestamp: {scanTime}\n"
        for item in results:
            if results[item] != 0:
                stringResult += f'\n Host: {item} is Not reachable [🟥]'
            else:
                stringResult += f'\n Host: {item} is up! [✅]'
        stringResult += f"\n{'-'*24}\n \n \n"
        file.write(stringResult)
        return stringResult
        

def ping(host,system):

    if system == "win":
        return os.system(f'ping {host} -n 1')
    else:
        return os.system(f'ping {host} -c 1')
    
def validateIP(ip):
   try:
       ipObj = ipaddress.ip_address(ip)
       return True
   except ValueError:
       return False

def validateDomain(hostname):
    if len(hostname) > 255:
        return False
    if hostname[-1] == ".":
        hostname = hostname[:-1] # strip exactly one dot from the right, if present
    allowed = re.compile("(?!-)[A-Z\d-]{1,63}(?<!-)$", re.IGNORECASE)
    return all(allowed.match(x) for x in hostname.split("."))

def getOs():
    if os.name == "nt":
        return "win"
    else:
        return "linux"

def main():
    os = getOs()
    count = 0
    results = dict()
    standardPingList = ["8.8.8.8","google.com"]
    #while count != 3:
    #    host = input("Enter IP or hostname: ")
    #    if validateIP(host):
    #        results[host] = ping(host,os)
    #        count += 1
    #    elif validateDomain(host):
    #        results[host] = ping(host,os)
    #        count += 1
    for i in range(len(standardPingList)):
        results[standardPingList[i]] = ping(standardPingList[i],os)
    
    print(writeToFile(results))
    

main()