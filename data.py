import urllib.request,urllib.parse,urllib.error
from urllib.request import Request,urlopen
from bs4 import BeautifulSoup
import requests
import ssl


#url = "http://192.168.42.234:51040/api/home/post_dataa"
url = "http://www.sasgamawre.online/api/home/post_dataa"
#ignore SSL certificate errors
def parse_data():
    ctx = ssl.create_default_context()
    ctx.check_hostname=False
    ctx.verify_mode = ssl.CERT_NONE
    url = 'https://www.investing.com/currencies/streaming-forex-rates-majors'
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    #------trying with requests
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url,headers=headers)
    #print("To r:",r)
    #print("To dir tou r",dir(r))
    #print("to type you r",type(r))
    #if r.ok:
        #print('hey there')
        #print('To status code:',r.status_code)
        #print('To url:',r.url)
        #print('To text:',r.text)
    #-------
    
    #r = urllib.request.urlopen(url,context=ctx).read()
    webpage = urlopen(req).read()

    #r.text is the content of the response in Unicode, and r.content is the
    #content of the response in bytes


    x = BeautifulSoup(r.text,'html.parser')
    symbols=dict()
    symbols1=list()
    for i in range(1,11):
        pair='#pair_'+str(i)
        pid='.pid-'+str(i)
        final_string=pair+' '+pid+'-'
        y=x.select_one(pair+' '+pid+'bid')
        symbol = x.select_one(pair+' .bold.left a').text
        bid = x.select_one(final_string+'bid').text
        ask = x.select_one(final_string+'ask').text
        high = x.select_one(final_string+'high').text
        low = x.select_one(final_string+'low').text
        Chg = x.select_one(final_string+'pc').text
        list1=[]
        #symbols[symbol]
        symbols1.append({'Name':symbol,'Bid':bid,'Ask':ask,'High':high,'Low':low,'Chg':Chg})
    #y = x.select_one('#pair_1 .pid-1-bid').text
    #symbol = x.select_one('#pair_1 .bold.left a')['title']
    #bid = x.select_one('#pair_1 .pid-1-bid').text
    #ask = x.select_one('#pair_1 .pid-1-ask').text
    #high = x.select_one('#pair_1 .pid-1-high').text
    #low = x.select_one('#pair_1 .pid-1-low').text
    #Chg = x.select_one('#pair_1 .pid-1-pc').text
    return symbols1
#pare ola ta fx prices!! kai valta se ena dictionary
#px 'EURUSD':{'Bid':1.1813,'Ask':1.1815,'High':1.1821,'Low':+0.0014,'Ch.%':+0.13%}




while True:
    list1=[]
    list1=parse_data()
    x = requests.post(url,json=list1)
    #symbols['EURUSD']={'Bid':bid,'Ask':ask,'Hight':high,'Low':low,'Chg':Chg}
    print(list1)
    print('#################################################################')

