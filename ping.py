import os

int = 0 # Integer for checking how many adresses is up.
packets = "1 "
wp = "ping -n " + packets #Windows ping
lp = "ping -c " + packets #Linux ping
space = "          "
#Adresses

customip1 = input("Enter Custom IP 1: ")
customip2 = input("Enter Custom IP 2: ")
customip3 = input("Enter Custom IP 3: ")

customrip1 = os.system(wp + customip1)
customrip2 = os.system(wp + customip2)
customrip3 = os.system(wp + customip3)

ip0 = "8.8.8.8" #Internet Connectivity
rip0 = os.system(wp + ip0)

ip1 = "google.com" # Example DNS adress
rip1 = os.system(wp + ip1)

ip2 = "vpn.spectoremote.com" #SpectoRemote AS VPN adress
rip2 = os.system(wp + ip2)



#adresses stop!
print("---------------------")
#Check if up or down!

if customrip1 == 0:
    print(space)
    print ("Custom IP 1: ", customip1, "is up!")
    int = int + 1
else:
    print(space)
    print ("Custom IP 1: ", customip1, "is down!")

if customrip2 == 0:
    print(space)
    print ("Custom IP 2: ", customip2, "is up!")
    int = int + 1
else:
    print(space)
    print ("Custom IP 2: ", customip2, "is down!")

if customrip3 == 0:
    print(space)
    print ("Custom IP 3: ", customip3, "is up!")
    int = int + 1
else:
    print(space)
    print ("Custom IP 3: ", customip3, "is down!")

if rip0 == 0:
  print(space)
  print (ip0, 'is up!')
  int = int + 1
else:
  print(space)
  print (ip0, 'is down!')

if rip1 == 0:
    print(space)
    print (ip1, "is up!")
    int = int + 1

else:
    print(space)
    print (ip1, "is down!")

if rip2 == 0:
    print(space)
    print (ip2, "is up!")
    int = int + 1
else:
    print(space)
    print (ip2, "is down!")



#Check how many adresses is up !


if int == 0:
    print(space)
    print("No adresses up! Check connectivity!")
else:
    print(space)
    print(int, "Adresses is up!")

if rip0 == 0:
    print(space)
    print("Internet is reachable!")
else:
    print("Internet is not reachable :-(")

if rip1 == 0:
    print("DNS is working!")
else:
    print("DNS is Not working !")

print("____________________________")
input("Press any key to exit... ")