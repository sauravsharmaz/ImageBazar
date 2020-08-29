from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import *
from django.shortcuts import redirect


def show_about_page(request):
	name = 'learn code with durgesh'
	link = 'https://www.youtube.com/learncodewithdurgesh'
	data = {'name':name,'link':link} 
	return render(request, "about.html", data) 

def show_home_page(request):
	cats = Category.objects.all()
	images = Image.objects.all()
	data = {'images': images, 'cats': cats}
	return render(request,"home.html",data) 

def show_category_page(request, cid):
	print(cid)
	cats = Category.objects.all() 
	category=Category.objects.get(pk=cid)
	images = Image.objects.filter(cat=category)
	data = {'images':images,'cats':cats}
	return render(request,"home.html",data) 


def  home(request):
	return redirect('/home')


