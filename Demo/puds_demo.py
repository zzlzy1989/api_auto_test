from suds.client import Client

#要访问的Webservice地址
url = "http://120.24.235.105:9010/sms-service-war-1.0/ws/smsFacade.ws?wsdl"
#创建Webservice Client对象
client = Client(url)
#print(client)可以打印出Client对象所有的方法
#print(client)

data = {"client_ip":"192.168.1.1","tmpl_id":"1","mobile":"17792303803"}
result = client.service.sendMCode(data)

print(result)