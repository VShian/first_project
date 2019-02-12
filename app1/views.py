from django.shortcuts import render
from django.views.generic import TemplateView
from app1.forms import ImageForm
from app1.models import Image

from PIL import Image as im
import pytesseract
import os
import re

def SaveImage(request):
	saved = False

	if request.method == 'POST':
		MyImageForm = ImageForm(request.POST, request.FILES)

		if MyImageForm.is_valid():
			image = Image()
			image.name = MyImageForm.cleaned_data['name']
			image.picture = MyImageForm.cleaned_data['picture']
			image.save()
			file = os.path.abspath('media/pictures/' + request.FILES['picture'].name)
			img = im.open(file)
			text = pytesseract.image_to_string(img,lang = 'eng')
			txt = text.split('\n')
			data=[]
			for word in txt:
				match = re.search(r'^[A-Z]+([,]*\s*[A-Z])*$',word)
				if match:
					data.append(match.group(0))
			print(data)
			saved = True
	else:
		MyImageForm = ImageForm()
	return render(request,'saved.html',locals())
