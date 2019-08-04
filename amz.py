import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.in/Neutrogena-Free-Acne-Face-175ml/dp/B006LXDMCS/ref=sr_1_3?crid=329XTSRTHR9DQ&keywords=nutregina+face+wash&qid=1562450073&s=gateway&sprefix=nutre%2Caps%2C512&sr=8-3'

headers = {"User-Agent":'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0'}

def check_price():

	page = requests.get(URL, headers=headers)

	soup = BeautifulSoup(page.content, 'html.parser')

	title = soup.find(id="productTitle").get_text()
	price = soup.find(id="priceblock_ourprice").get_text()
	converted_price = float(price[2:5])

	if(converted_price<440):
		send_mail()

	print(converted_price)
	print(title.strip())

def send_mail():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('shashankk.mitraa14002@gmail.com', 'rmqcovawzawzkvfk')

	subject = 'DUDE Price fell down'
	body = 'Check amazon link https://www.amazon.in/Neutrogena-Free-Acne-Face-175ml/dp/B006LXDMCS/ref=sr_1_3?crid=329XTSRTHR9DQ&keywords=nutregina+face+wash&qid=1562450073&s=gateway&sprefix=nutre%2Caps%2C512&sr=8-3'

	msg = f"Subject: {subject}\n\n{body}"

	server.sendmail(
		'shashankk.mitraa14002@gmail.com',
		'shashankmittra@jklu.edu.in',
		msg
		)

	print('EMAIL HAS BEEN SENT')

	server.quit()


check_price()