import requests,socket,os,keyboard,time

web_user = input("Enter a website: ")

https = 'https://'

web_to_ip = socket.gethostbyname(web_user)

print(f'website, {web_user} -> ip [{web_to_ip}]')

print('Pinging to see if connection is valid\n')



        # status code start
def requestStatusCode(findWeb):
    
    r = requests.get(findWeb)
    
    if r.status_code == 200:
        print(f'website, {addition} -> {r.status_code}, [{web_to_ip}]\nVALID!\n')
        
    else:
        print(f'Status code invalid [{r.status_code}]')
            # status code end



def inspectWeb(website):
    
  
    r = requests.get(website)
    
    print(r.text)                   # like inspect element



#ping start
os.system(f'ping {web_to_ip}')

time.sleep(3)

keyboard.is_pressed('ctrl+c')

print('Ping ended!\n')
#ping end

userDir = input("Enter valid url pathway: ")

addition = https+web_user+userDir

requestStatusCode(findWeb=addition)     # users dir here

see = input("Inspect web? y/n: ")

if see == 'Y'.lower():
    inspectWeb(website=addition)
    
elif see == 'N'.lower():
    print('Exiting...')
    
else:
    print(f'{see} is not a valid input!')