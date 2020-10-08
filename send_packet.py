import requests
import json
import get_cookie
import random

import time
import os

def tmp():  #用于生成随机体温
    a=str(round(random.uniform(35.8, 37.2),1))
    return a
url="http://ncp.suse.edu.cn/api/questionnaire/questionnaire/addMyAnswer"
headers={
"Host":"ncp.suse.edu.cn",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0",
"DNT":"1",
"Content-Type":"application/json",
"Accept":"*/*",
"Origin":"http://ncp.suse.edu.cn",
"Referer":"http://ncp.suse.edu.cn/questionnaire/addanswer?page_from=onpublic&activityid=82&can_repeat=1",
"Accept-Encoding":"gzip, deflate",
"Accept-Language":"zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
"Cookie":"whistle-spaserver="+get_cookie.cookie['web-whistle'],
"Connection":"close"
}
queastion=[
{"questionid":987,"optionid":"1794","optiontitle":"已返校","question_sort":0,"question_type":1,"option_sort":0,"range_value":"","content":"","isotheroption":0,"otheroption_content":"","isanswered":True,"answerid":0,"answered":True},
{"questionid":996,"optionid":"1816","optiontitle":"在校","question_sort":0,"question_type":1,"option_sort":0,"range_value":"","content":"","isotheroption":0,"otheroption_content":"","isanswered":True,"answerid":0,"answered":True},
{"questionid":998,"optionid":"1818","optiontitle":"没有出现症状","question_sort":0,"question_type":2,"option_sort":0,"range_value":"","content":"","isotheroption":0,"otheroption_content":"","isanswered":True,"answerid":0,"answered":True},
{"questionid":999,"optionid":"1825","optiontitle":"否，身体健康 ","question_sort":0,"question_type":1,"option_sort":0,"range_value":"","content":"","isotheroption":0,"otheroption_content":"","isanswered":True,"answerid":0,"answered":True},
{"questionid":1000,"optionid":0,"optiontitle":0,"question_sort":0,"question_type":10,"option_sort":0,"range_value":"","content":tmp(),"isotheroption":0,"otheroption_content":"","isanswered":True,"answerid":0,"answered":True},
{"questionid":1001,"optionid":0,"optiontitle":0,"question_sort":0,"question_type":10,"option_sort":0,"range_value":"","content":tmp(),"isotheroption":0,"otheroption_content":"","isanswered":True,"answerid":0,"answered":True},
{"questionid":1002,"optionid":0,"optiontitle":0,"question_sort":0,"question_type":10,"option_sort":0,"range_value":"","content":tmp(),"isotheroption":0,"otheroption_content":"","isanswered":True,"answerid":0,"answered":True},
{"questionid":1003,"optionid":"1830","optiontitle":"是","question_sort":0,"question_type":1,"option_sort":0,"range_value":"","content":"","isotheroption":0,"otheroption_content":"","isanswered":True,"answerid":0,"answered":True}
]
arr=[
{"questionid":987,"optionid":"1794","optiontitle":"已返校","question_sort":0,"question_type":1,"option_sort":0,"range_value":"","content":"","isotheroption":0,"otheroption_content":"","isanswered":True,"answerid":0,"answered":True},
{"questionid":988,"optionid":0,"optiontitle":0,"question_sort":0,"question_type":8,"option_sort":0,"range_value":"","content":"","isotheroption":0,"otheroption_content":"","isanswered":"","answerid":0,"hide":True,"answered":False},
{"questionid":989,"optionid":0,"optiontitle":0,"question_sort":0,"question_type":7,"option_sort":0,"range_value":"","content":"","isotheroption":0,"otheroption_content":"","isanswered":"","answerid":0,"hide":True,"answered":False},
{"questionid":990,"optionid":0,"optiontitle":0,"question_sort":0,"question_type":1,"option_sort":0,"range_value":"","content":"","isotheroption":0,"otheroption_content":"","isanswered":"","answerid":0,"hide":True,"answered":False},
{"questionid":991,"optionid":0,"optiontitle":0,"question_sort":0,"question_type":4,"option_sort":0,"range_value":"","content":"","isotheroption":0,"otheroption_content":"","isanswered":"","answerid":0,"hide":True,"answered":False},
{"questionid":992,"optionid":"","optiontitle":"","question_sort":0,"question_type":2,"option_sort":0,"range_value":"","content":"","isotheroption":0,"otheroption_content":"","isanswered":"","answerid":0,"hide":True,"answered":False},
{"questionid":993,"optionid":"","optiontitle":"","question_sort":0,"question_type":2,"option_sort":0,"range_value":"","content":"","isotheroption":0,"otheroption_content":"","isanswered":"","answerid":0,"hide":True,"answered":False},
{"questionid":994,"optionid":0,"optiontitle":0,"question_sort":0,"question_type":10,"option_sort":0,"range_value":"","content":"","isotheroption":0,"otheroption_content":"","isanswered":"","answerid":0,"hide":True,"answered":False},
{"questionid":995,"optionid":0,"optiontitle":0,"question_sort":0,"question_type":1,"option_sort":0,"range_value":"","content":"","isotheroption":0,"otheroption_content":"","isanswered":"","answerid":0,"hide":True,"answered":False},
{"questionid":996,"optionid":"1816","optiontitle":"在校","question_sort":0,"question_type":1,"option_sort":0,"range_value":"","content":"","isotheroption":0,"otheroption_content":"","isanswered":True,"answerid":0,"answered":True},
{"questionid":997,"optionid":0,"optiontitle":0,"question_sort":0,"question_type":4,"option_sort":0,"range_value":"","content":"","isotheroption":0,"otheroption_content":"","isanswered":"","answerid":0,"hide":True,"answered":False},
{"questionid":998,"optionid":"1818","optiontitle":"没有出现症状","question_sort":0,"question_type":2,"option_sort":0,"range_value":"","content":"","isotheroption":0,"otheroption_content":"","isanswered":True,"answerid":0,"answered":True},
{"questionid":999,"optionid":"1825","optiontitle":"否，身体健康 ","question_sort":0,"question_type":1,"option_sort":0,"range_value":"","content":"","isotheroption":0,"otheroption_content":"","isanswered":True,"answerid":0,"answered":True},
{"questionid":1000,"optionid":0,"optiontitle":0,"question_sort":0,"question_type":10,"option_sort":0,"range_value":"","content":tmp(),"isotheroption":0,"otheroption_content":"","isanswered":True,"answerid":0,"answered":True},
{"questionid":1001,"optionid":0,"optiontitle":0,"question_sort":0,"question_type":10,"option_sort":0,"range_value":"","content":tmp(),"isotheroption":0,"otheroption_content":"","isanswered":True,"answerid":0,"answered":True},
{"questionid":1002,"optionid":0,"optiontitle":0,"question_sort":0,"question_type":10,"option_sort":0,"range_value":"","content":tmp(),"isotheroption":0,"otheroption_content":"","isanswered":True,"answerid":0,"answered":True},
{"questionid":1003,"optionid":"1830","optiontitle":"是","question_sort":0,"question_type":1,"option_sort":0,"range_value":"","content":"","isotheroption":0,"otheroption_content":"","isanswered":True,"answerid":0,"answered":True}
]
POSTDATA=json.dumps({
"sch_code":"suse",
"stu_code":get_cookie.response_data.get("student_number"),
"stu_name":get_cookie.response_data.get("name"),
"identity":get_cookie.response_data.get("identity"),
"path": get_cookie.response_data.get('orgPath')[1]['organization_id']+","+get_cookie.response_data.get('orgPath')[2]['organization_id']+","+get_cookie.response_data.get('orgPath')[3]['organization_id']+","+get_cookie.response_data.get('orgPath')[4]['organization_id']+","+get_cookie.response_data.get('orgPath')[5]['organization_id'],
"organization":get_cookie.org_data[0]['org_name'][0]+"&0/"+get_cookie.org_data[0]['org_name'][1]+"&3/"+get_cookie.org_data[0]['org_name'][2]+"&1/"+get_cookie.org_data[0]['org_name'][3]+"&0/"+get_cookie.org_data[0]['org_name'][4]+"&0",
"gender":get_cookie.response_data.get("sex"),
"activityid":"82",
"anonymous":0,
"canrepeat":1,
"repeat_range":1,
"question_data":queastion,
"totalArr":arr,
"private_id":0
})
rr=requests.post(url,headers=headers,data=POSTDATA)
print(rr.status_code)
print(rr.text)
result = open("result.txt","w")
result.write(str(rr.status_code))
result.write(rr.text)
result.close()
time.sleep(5)
