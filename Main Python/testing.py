import requests,socket,os,keyboard,time

web_user = input("Enter a website: ")

https = 'https://'

web_to_ip = socket.gethostbyname(web_user)

print(f'website, {web_user} -> ip [{web_to_ip}]')

print('Pinging to see if connection is valid\n')



        # status code start
def requestStatusCode(findWeb):
    
    r = requests.get(findWeb)
    
    try:
        
        if r.status_code == 200:
            print(f'Valid connection, [{web_to_ip}]')
    
    except Exception as e:
        print(f'Invalid, [{r.status_code}]')
        
            # status code end



def inspectWeb(website):
    
    try:
        r = requests.get(website)
        
        print(r.text)                   # like inspect element
    
    except Exception as e:
        print(f'[ERROR] -> {e}')



#ping start
os.system(f'ping {web_to_ip}')

time.sleep(3)

keyboard.is_pressed('ctrl+c')

print('Ping ended!\n')
#ping end

userDir = input("Enter valid url pathway: ")

requestStatusCode(findWeb=f'{https+web_user+userDir}')     # users dir here
inspectWeb(website=f'{https+web_user+userDir}')