import requests

w1 = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=300&country=all&ssl=all&anonymity=all', allow_redirects=True).content
w2 = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=https&timeout=300&country=all&ssl=all&anonymity=all', allow_redirects=True).content
w3 = requests.get('https://api.proxyscrape.com/?request=displayproxies&protocol=https&timeout=300&country=all&ssl=all&anonymity=all', allow_redirects=True).content
w4 = requests.get('https://api.proxyscrape.com/?request=displayproxies&protocol=https&timeout=300&country=all&ssl=all&anonymity=all', allow_redirects=True).content
w5 = requests.get('https://raw.githubusercontent.com/duongpokee/adsasd/main/hfjda.txt', allow_redirects=True).content

# try:
# 	with open('px.txt','a') as f:
# 		f.write(w1.content)
# 		f.write(w2.content)
# 		f.write(w3.content)
# 		f.write(w4.content)
# 		f.write(w5.content)
# 		f.close()
# except:
# 	print("EROR")

f = open('proxies.txt', 'wb')
f.write(w1)
f.write(w2)
f.write(w3)
f.write(w4)
f.write(w5)
f.close()

print('GET PROXY COMPLETE!')
m1 = requests.get('https://raw.githubusercontent.com/duongpokee/adsasd/main/dfsdfds', allow_redirects=True).content
f = open('messages.txt', 'wb')
f.write(m1)
print('GET MESSAGES COMPLETE!')