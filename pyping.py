from datetime import datetime
import os
import platform

# Open pingresults.txt
File_object = open(r"pingresults.txt", "a+")
# strings
# change -n to -c for linux compatability
packets = (" -n 1 ")
dns = ("google.com")
internet = ("8.8.8.8")
ip1up = 1
ip2up = 1
ip3up = 1
ping = ("ping")
dnsup = 1
internetup = 1
ip1 = input("Input IP adress to ping: ")
ip2 = input("Input second IP to ping: ")
ip3 = input("Input third IP to ping: ")
# actual ping command

# Prettifier for the result.txt
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
File_object.write("\n" * 3)
File_object.write("Results from the latest scan ")
File_object.write(dt_string)

res1 = os.system(ping + packets + ip1)
if res1 == 0:
    print(ip1, 'is up!')
    result1 = (ip1 + " is up!")
    File_object.write("\n")
    File_object.write(result1)
    ip1up += 1
else:
    print(ip1, 'is down!')
    result1 = (ip1 + " is  down!")
    File_object.write("\n")
    File_object.write(result1)
    ip1up -= 1
# Ping number 2
res2 = os.system(ping + packets + ip2)
if res2 == 0:
    print(ip2, 'is up!')
    result2 = (ip2 + " is up!")
    File_object.write("\n")
    File_object.write(result2)
    ip2up += 1
else:
    print(ip2, 'is down!')
    result2 = (ip2 + " is  down!")
    File_object.write("\n")
    File_object.write(result2)
    ip2up -= 1
# Ping number 3
res3 = os.system(ping + packets + ip3)
if res3 == 0:
    print(ip3, 'is up!')
    result3 = (ip3 + " is up!")
    File_object.write("\n")
    File_object.write(result3)
    ip3up += 1
else:
    print(ip3, 'is down!')
    result3 = (ip3 + " is  down!")
    File_object.write("\n")
    File_object.write(result3)
    ip3up -= 1

res4 = os.system(ping + packets + dns)
if res4 == 0:
    print(dns, 'is up!')
    result4 = ("DNS is working!")
    File_object.write("\n")
    File_object.write(result4)
    dnsup += 1
else:
    print(dns, 'is down!')
    result4 = ("DNS is not working propperly!")
    File_object.write("\n")
    File_object.write(result4)
    dnsup -= 1

res5 = os.system(ping + packets + internet)
if res5 == 0:
    print(internet, 'is up!')
    result5 = ("You have a connection to the world wide web")
    File_object.write("\n")
    File_object.write(result5)
    internetup += 1
else:
    print(internet, 'is down!')
    result5 = ("You have no connection to the world wide web!")
    File_object.write("\n")
    File_object.write(result5)
    internetup -= 1

print("_" * 24)
print("Results")
print("_" * 24)
if ip1up == 2:
    print(ip1, " is up")
else:
    print(ip1, " is down")

if ip2up == 2:
    print(ip2, " is up")
else:
    print(ip2, " is down")

if ip3up == 2:
    print(ip3, " is up")
else:
    print(ip3, " is down")

if dnsup == 2:
    print("DNS is working!")
else:
    print("DNS is not working propperly!")

if internetup == 2:
    print("You have internet connection!")
else:
    print("Cannot reach the World Wide Web!")

print("_" * 24)
# close pingresults
File_object.close()
