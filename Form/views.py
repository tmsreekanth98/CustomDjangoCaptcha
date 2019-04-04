# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,HttpResponseRedirect
from .models import Info
from .forms import InputForm,Captcha_InputForm
from PIL import Image, ImageDraw, ImageFont
import random,string

def homepage(req):
	status = "N"
	if req.method == 'POST':
		form = InputForm(req.POST)

		if form.is_valid():
			name = form.cleaned_data['Name']
			roll_no = form.cleaned_data['Roll_No']
			info_obj = Info()
			info_obj.name = name
			info_obj.roll_no = roll_no
			info_obj.save()
			status = Info.objects.all().count()
	else:
		form = InputForm()

	return render(req,'Form/index.html',{'form':form,'status':status})



def captcha(req):
	status = "N"
	if req.method == 'POST':
		form = Captcha_InputForm(req.POST)

		if form.is_valid():
			name = form.cleaned_data['Name']
			roll_no = form.cleaned_data['Roll_No']
			cp = form.cleaned_data['Captcha']

			if cp.lower() != req.session['cp'].lower():
				form = Captcha_InputForm()
				status = "Incorrect_Captcha"
			else:
				info_obj = Info()
				info_obj.name = name
				info_obj.roll_no = roll_no
				info_obj.save()
				status = Info.objects.all().count()
			generateCaptcha(req)

	else:
		form = Captcha_InputForm()
		#Generating captcha
		generateCaptcha(req)

	return render(req,'Form/index.html',{'form':form,'status':status})




def generateCaptcha(req):
	font_type = random.randint(2,4)
	if font_type == 2:
		f = 'Form/' + str(font_type) + '.otf'
	else:
		f = 'Form/' + str(font_type) + '.ttf' 
	
	captcha = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=random.randint(5,9)))

	req.session['cp'] = captcha
	
	print(captcha)

	req.session.modified = True

	img = Image.new('RGB', (200, 60), color = (16, 16, 16))
	fnt = ImageFont.truetype(f, 35)
	d = ImageDraw.Draw(img)
	d.text((15,15), captcha, font=fnt, fill=(255, 255, 0))
	 
	img.save('Form/static/Form/img/cp.png')