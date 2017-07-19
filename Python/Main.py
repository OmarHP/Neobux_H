import requests
import logging
import http.client as http_client

from bs4 import BeautifulSoup


# http_client.HTTPConnection.debuglevel = 1
# You must initialize logging, otherwise you'll not see debug output.
# logging.basicConfig()
# logging.getLogger().setLevel(logging.DEBUG)
# requests_log = logging.getLogger("requests.packages.urllib3")
# requests_log.setLevel(logging.DEBUG)
# requests_log.propagate = True


USER_AGENT = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Mobile Safari/537.36'



session = requests.Session()
session.headers.update({'user-agent':USER_AGENT})

response = session.get('https://www.neobux.com/')
cookies = requests.utils.dict_from_cookiejar(session.cookies)

htmlIndex = response.text
soup = BeautifulSoup(htmlIndex, 'html.parser')
links = soup.select('a[onclick]')
loginLink = links[0]
urlLoginForm = loginLink['onclick']
urlLoginForm = urlLoginForm[urlLoginForm.index('\'') + 1: urlLoginForm.rindex('\'')]
print(urlLoginForm)

# headers['referer'] = 'https://www.neobux.com/'
# headers['authority'] = 'www.neobux.com'
# headers['scheme'] = 'https'
# headers['path'] = urlLoginForm.replace('https://www.neobux.com', '')
# headers['accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
# headers['accept-encoding'] = 'gzip, deflate, sdch, br'
# headers['accept-language'] = 'es-419,es;q=0.8'
# headers['upgrade-insecure-requests'] = '1'
# print(headers)

response = session.get(urlLoginForm, cookies=cookies)
cookies = requests.utils.dict_from_cookiejar(session.cookies)

htmlLoginForm = response.text
soup = BeautifulSoup(htmlLoginForm, 'html.parser')

userParamName = soup.select('#Kf1')[0]['name']
password1ParamName = soup.select('#Kf2')[0]['name']
hiddenParamName = soup.select('#Kf3')[0]['name']
password2ParamName = soup.select('#Kf4')[0]['name']

lgeValue = soup.select("input[name='lge']")[0]['value']
urlDoLogin = soup.select('#loginform')[0]['action']


data = {userParamName: 'xxxx', password1ParamName:'xxxx', password2ParamName: 'xxxx', hiddenParamName:'sth', 'lge':lgeValue, 'login':1}

r = requests.post("http://httpbin.org/post", data=data, cookies=cookies)
print(r.text)

response = session.post(urlDoLogin, data=data, cookies=cookies)
htmlHome = response.text
soup = BeautifulSoup(htmlHome, 'html.parser')
print(soup.select('.f_r')[0])


