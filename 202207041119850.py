from random import randint
import requests
import re
import time

def toStr(page,type):
    if type==0:
        return str(page).zfill(6)
    if type==1:
        return "cov"+str(page).zfill(3)
    if type==2:
        return "bok"+str(page).zfill(3)
    if type==3:
        return "leg"+str(page).zfill(3)
    if type==4:
        return "fow"+str(page).zfill(3)
    if type==5:
        return "!"+str(page).zfill(5)

urll="http://jiaocai1.lib.xjtu.edu.cn:9088/jpath/reader/reader.shtml?channel=100&code=1fc1befdbece4f5e55dff09fb7f899d4&cpage=1&epage=-1&ipinside=0&netuser=0&spage=1&ssno=11192431"
aPage =1
bPage =1
PageType=2#1：封皮cov 2:扉页bok 3:简介leg 4:序言fow 5:目录! 0:正文
cookie ='jiagong=FB2C992B7935D5D86152D38397FC7CCF'
heads = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'Cookie':cookie
    }
r = requests.get(urll,headers=heads)
re1="var opts = {(.*?)}"
re2="jpgPath: \"(.*?)\""
a=re.findall(re1,r.text,re.S|re.M|re.DOTALL)
if a == None:
    print("cookie错误，请重试")
    exit(0)
b=re.findall(re2,a[0],re.S|re.M|re.DOTALL)
heads = {
    'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'DNT': '1',
    'Cookie':cookie,
    'Referer':urll
    }
jpgPath='http://jiaocai1.lib.xjtu.edu.cn:9088/jpath/'+b[0]
while aPage<=bPage:
    pageStr=toStr(aPage,PageType)
    jpgUrl = jpgPath + pageStr + ".jpg?zoom=0"
    print(pageStr)
    photo=requests.get(jpgUrl,headers=heads)
    print(photo.headers['content-length'])
    if photo.headers["content-length"]==0 or photo.status_code !=200:
        print("超出限制，程序退出")
        exit(0)
    with open("./photo/"+pageStr+".png","x") as f:
        f.write(photo.content)
    aPage+=1
    #time.sleep(randint(3,60))
'''
r = requests.get(jpgPath,headers=heads,cookies=cookie)
print(jpgUrl)
print(r.status_code)
'''