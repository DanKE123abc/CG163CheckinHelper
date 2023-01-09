import time
import json
import setting
import requests
import wechatpush

#时间：2023/1/9
#作者：蛋壳
#Another: DanKe
#备注：网易云游戏自动签到

sign_url = setting.Sign_url
current = setting.Current
headers = setting.headers

def buildHeaders(authorization):#更改headers
    headers["Authorization"] = authorization

def sign():#签到
    result = requests.post(url=sign_url, headers=headers)
    return result

def check():#验证
    result = requests.get(url=current, headers=headers)
    return result

def writeMsg():#编辑信息
    checkReturn = check()
    if checkReturn.status_code == 200:
        checkResult = "成功"
        signReturn = sign()
        if signReturn.status_code == 200:
            signResult = "成功"
        elif signReturn.status_code == 400:
            signResult = "你已经签到过了"
        else:
            signResult = "失败，code="+str(signReturn.status_code)+"，请通过code判断失败原因"
    elif checkReturn.status_code == 401:
        checkResult = "登录信息可能已经失效"
        signResult = "账号验证失败，无法签到"
    else:
        checkResult = "失败，code="+str(checkReturn.status_code)+"，请通过code判断失败原因"
        signResult = "账号验证失败，无法签到"
    message = '''⏰当前时间：{} 
您今天签到网易云游戏了吗？
####################
🧐账号验证：{}
💻签到结果：{}
####################
祝您过上美好的一天！

     ——by DanKe'''.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() + 28800)),
                        checkResult,
                        signResult)
    return message



def handler(event, context):#这里是阿里云的入口，腾讯云要改成main_handler
    config_path = "config.json"
    with open(config_path, "r") as f:
        row_data = json.load(f)
    for user in row_data:
        authorization = user['Authorization']
        pushid = user['pushid']
        try:
            buildHeaders(authorization)
            msg = writeMsg()
        except:
            msg = '签到失败，Authorization可能发生错误'
            msg_en = 'Check in failed,possible error in Authorization'
            print(msg)
            print(msg_en)
        if setting.WechatPush == True :
            wechatpush.push_text(pushid, msg)
        elif setting.WechatPush == False :
            print("微信推送功能未启用")
            print('WeChatPush is not enabled')

if __name__ == '__main__':
    handler(None, None)
