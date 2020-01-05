import urllib.request
import urllib.parse
import json

content = input("please input the content you want to translate!\n")

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
data = {}
data['i'] = content
data['from']= 'AUTO'
data['to']= 'AUTO'
data['smartresult']= 'dict'
data['client']= 'fanyideskweb'
data['salt']='15782289425979'
data['sign']='e5bb30ce0abda85da13a4835d187b3e6'
data['ts']='1578228942597'
data['bv']='ca3dedaa9d15daa003dbdaaa991540d1'
data['doctype']='json'
data['version']='2.1'
data['keyfrom']='fanyi.web'
data['action']='FY_BY_CLICKBUTTION'

data = urllib.parse.urlencode(data).encode('utf-8')
reponse = urllib.request.urlopen(url,data)

html = reponse.read().decode('utf-8')
target = json.loads(html)
print("翻译结果： %s\n" %(target['translateResult'][0][0]['tgt']))


