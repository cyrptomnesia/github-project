import os,socket,requests,subprocess

# -- setting up the basics
pathCache = os.path.expandvars('%userprofile%')
mainCachePath = os.path.expanduser(pathCache)
https = 'https://'


# -- setting up the targetted web
input_websiteIP = input("Enter a website dns: ")
webIP = socket.gethostbyname(input_websiteIP)



print(f'initial web, [{input_websiteIP}] -> ip [{webIP}]')



# -- checking the validity of the connection again, but shows the status incase if there is just a 404 or something lmao
def reqFindValidConnection(reqIP):
    
    req = requests.get(reqIP)

    try:
    
        if req.status_code == 200:
            print(f'Valid Connection! [{req.status_code}]')
            return req.status_code
            
        else:
            print(f'Something has happened in the netwrok! [{req.status_code}]')

    except requests.ConnectionError:
        print('[!] Broken network')
        quit()


def ezPing():
    
    os.system(f'ping {webIP} > {mainCachePath}\\writeME.txt')


# -- storing data
with open(f'{mainCachePath}\\writeME.txt','w') as f:
    
    f.write(f"web [{input_websiteIP}] -> ip, [{webIP}]\nStatus code -> {reqFindValidConnection(reqIP=https+input_websiteIP)}\n")
    f.close()