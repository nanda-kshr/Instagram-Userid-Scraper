import requests
import time
#fff = open("idsUser.txt","w")

fff = open("idsUser.txt","a")

session = input("session - check youtube if you dont know about instagram session")
cookies = {
    'ig_nrcb': '1',
    'mid': 'Ytp9sgABAAEr3s0_2YZo4_XrBDmF',
    'ig_did': 'EF3EF3F3-2BFA-4468-82AE-4A63DE12C163',
    'csrftoken': 'h9vf5RqN4Yl9idwz90th4sl3mZ0duupl',
    'ds_user_id': '50549400865',
    'sessionid': str(session),
    'shbid': '"19028\\05450549400865\\0541690022225:01f7463b7479e4cb68363b580320b2bd34f4bf58e0b2e7db477f59a721791a3065424fff"',
    'shbts': '"1658486225\\05450549400865\\0541690022225:01f7330e75353242a634c9bc68bf92a871d6bba2948440863ef591941020a09293bb99e3"',
    'dpr': '3',
    'datr': '4n3aYn-bhY8KT8xSZYSIfl3l',
    'rur': '"RVA\\05450549400865\\0541690022392:01f7eec25e9967bf344a1198e0bc0adbd4f74c36dd1cfdf912a828ea5ca2db8cc3086ef6"',
}

headers = {
    'authority': 'i.instagram.com',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/',
    'user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1831) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
    'viewport-width': '360',
    'x-asbd-id': '198387',
    'x-csrftoken': 'h9vf5RqN4Yl9idwz90th4sl3mZ0duupl',
    'x-ig-app-id': '1217981644879628',
    'x-ig-www-claim': 'hmac.AR1lFVsHGZeq1W-0kNXZNAjWgdDUsZrElLKDrKDvHk1WZ7-E',
}
kolo = ''
count = 1
k = 0
def run():
    global kolo, count, k
    try:
        params = {
            'count': '20942',
            'max_id': kolo,
            'search_surface': 'follow_list_page',
        }

        response = requests.get('https://i.instagram.com/api/v1/friendships/44193286312/followers/', params=params, cookies=cookies, headers=headers).json()
        k = 0
        kolo = response['next_max_id']

        for items in response['users']:
            userid = response['users'][k]['pk']
            username = response['users'][k]['username']
            user = {"userid": str(userid), "username": username}
            print(f'{userid}  :  {username} ')
            
            fff.write(str(userid)+"\n")
          
            k = k + 1

    except Exception as e:
        print(e)
    time.sleep(60)
        
        
while True:
    run()
    fff.close()
    
