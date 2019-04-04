import mechanize 
import random,string

n=50
while n>0:
	br = mechanize.Browser() 
	br.set_handle_robots(False) 
	bot = br.open("http://localhost:8000/captcha")
	br.select_form(nr=0)
	br["Name"]=''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=6))
	br["Roll_No"]=''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=6))
	br["Captcha"]=''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=6))
	sign_up = br.submit()
	n=n-1


