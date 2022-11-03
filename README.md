# CG163CheckHelper

![Language](https://img.shields.io/badge/Language-Python-yellow)![LICENSE](https://img.shields.io/badge/LICENSE-GPL--3.0-red)![Author](https://img.shields.io/badge/Author-DanKe-blue)

网易云游戏自动签到，白嫖免费时长，使用微信订阅号推送信息。

### 起因

懒 + 健忘

所以写了个程序自动签到

### 安装教程

##### 1.获取 authorization

（这里浏览器使用的是Windows上的Edge）

​    进入已经登录账号的[网易云游戏网站](http://cg.163.com)，按 `F12` 打开开发者工具，点击网络一栏

​    刷新一下网站，然后找到 `@me` 一项 (没有的话换一个)，复制请求标头中的`authorization`一项

##### 2.登录微信公众平台：[微信公众平台 (qq.com)](https://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=sandbox/login)

​	获得你的微信测试号，在./setting.py里修改`appid`与`appsecret`即可

​	关注你的微信测试号，得到你的推送id（`pushid`）

##### 3.配置信息

​    在./config.json里修改用户信息

​    支持多用户

### 待续

todo
