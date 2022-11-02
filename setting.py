

#--------------------推送设置-----------------------

WechatPush= True
APPID = ""
APPSECRET = ""



#------------------网易云游戏设置--------------------
Sign_url = 'https://n.cg.163.com/api/v2/sign-today'
Current = 'https://n.cg.163.com/api/v2/client-settings/@current'
UserAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.26'










#--------------------以下非特殊情况不要动---------------------
headers = {
    'Authorization': '', 
    'Connection': 'keep-alive',
    'Content-Length': '0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja-JP;q=0.6,ja;q=0.5',
    'Host': 'n.cg.163.com',
    'Origin': 'https://cg.163.com',
    'Referer': 'https://cg.163.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': UserAgent,
    'X-Platform': '0'
    }
