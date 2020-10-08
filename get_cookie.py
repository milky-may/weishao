import requests
from requests.cookies import RequestsCookieJar
import json
import sys

result=[]
with open('accounts.txt','r') as f:
	for line in f:
		result.append(list(line.strip('\n').split(',')))

url="http://web.weishao.com.cn/api/login"
headers={
'Host':'web.weishao.com.cn',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3739.400',
'DNT':'1',
'Content-Type':'application/json',
'Accept':'*/*',
'Origin':'http://web.weishao.com.cn',
'Referer':'http://web.weishao.com.cn/login',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
'Connection':'close'
}

module_array=["userInfo","accountSafe","schoolCard","about","feedback","setting","contacts"],
module_name=["","","","","","",""],
module_name_en=["","","","","","",""],

POSTDATA=json.dumps({
    "name":result[0][0],
    "password":result[1][0],
    "school":{
        "search_pinyin":".scqhgdx.sichuanqinghuagongdaxue.sichuanqinghuagongdaixue.",
        "school_num":"",
        "name":"四川轻化工大学",
        "domain":"suse",
        "pinyin":"sichuanqinghuagongdaxue",
        "and_umeng_app_key":"55d19d74e0f55a02960038a5",
        "and_umeng_app_secret":"6f2ac4756ebc4dfbb1ca8893125a67b8",
        "ios_umeng_app_key":"55d19e7667e58e182b001a19",
        "ios_umeng_app_secret":"qx0crqzhadgruicjcs2dxqfjqrg8fjjb",
        "config_update_time":"2020-07-24 10:22:51",
        "offset_map_x":"104.771668",
        "offset_map_y":"29.338200",
        "ex_field":{
            "school_top_flag":"schoollogo",
            "school_top_url":{
                "default":{"img":"null","words":""},
                "schoollogo":{"img":"http://store.weishao.com.cn//group1/M00/20/05/rBGLH14-ZFeAcByqAAG80V5l0w0802.png","words":"四川轻化工大学"},
                "customer":{"img":"","words":""}
            }
        },
        "configLoaded":True,
        "config":{
            "app_url":"null",
            "offset_map_x":"104.771668",
            "offset_map_y":"29.338200",
            "is_scores":"0",
            "search_pinyin":".scqhgdx.sichuanqinghuagongdaxue.sichuanqinghuagongdaixue.",
            "school_num":"",
            "name":"四川轻化工大学",
            "domain":"suse",
            "pinyin":"sichuanqinghuagongdaxue",
            "url_crash_upload":"http://172.16.56.175/report/?mod",
            "url_download":"http://store.weishao.com.cn/",
            "url_main_server":"https://service.weishao.com.cn/whistlenew/index.php",
            "url_upload":"http://store.weishao.com.cn//image/upload2",
            "and_umeng_app_key":"55d19d74e0f55a02960038a5",
            "and_umeng_app_secret":"6f2ac4756ebc4dfbb1ca8893125a67b8",
            "ios_umeng_app_key":"55d19e7667e58e182b001a19",
            "ios_umeng_app_secret":"qx0crqzhadgruicjcs2dxqfjqrg8fjjb",
            "config_update_time":"2020-07-24 10:22:51",
            "memo":" * ",
            "api_server":"http://lightapp.weishao.com.cn/linkshare/NewsClient.do?",
            "QRUrl":"http://login.weishao.com.cn/index.html?ver=1",
            "icon_url":"http://store.weishao.com.cn//group1/M00/20/05/rBGLH14-ZFeAcByqAAG80V5l0w0802.png",
            "campuscard_bgd_img":"",
            "disclaimer":{},
            "memo_ex":"null",
            "campuscard_bgd_img_new":{},
            "ex_field":{
                "school_top_flag":"schoollogo",
                "school_top_url":{
                    "default":{"img":"null","words":""},
                    "schoollogo":{"img":"http://store.weishao.com.cn//group1/M00/20/05/rBGLH14-ZFeAcByqAAG80V5l0w0802.png","words":"四川轻化工大学"},
                    "customer":{"img":"","words":""}
                }
            },
            "customized":"0",
            "client_config":"{\"web_config\":{\"basicConfig\":{\"color\":\"#0dac67\"},\"imgUrlKeys\":[{\"text\":\"logo_icon\"}]}}",
            "app_cfg":{
            "version_url":"https://cms.weishao.com.cn/versions/",
            "cloudGround_status":1,
            "bind_tell":"null",
            "bind_mail":"null",
            "user_center":"null",
            "protocol_url":"https://cms.weishao.com.cn/agreements/",
            "password_change":"null",
            "reset_pwd_url":1,
            "account_security_url":1,
            "login_bind":1,
            "module_array":module_array,
            "module_name":module_name,
            "module_name_en":module_name_en,
            "password_url":"null",
            "bind_phone_url":"https://xiaoyuan.weishao.com.cn/weishao/plain?"
            },
            "uploadurl_hx":"https://download.weishao.com.cn/uploadfile",
            "uploadurl_overtime":180,
            "originalDomain":"suse"
        }
    }
})
r=requests.post(url,headers=headers,data=POSTDATA)
cookie=requests.utils.dict_from_cookiejar(r.cookies) #将cookie转化为字典
response_data=json.loads(r.text)
org_data=response_data.get("title")
