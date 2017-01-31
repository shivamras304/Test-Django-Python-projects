from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from models import MyData

# Create your views here.

def main_page(request):
	return render(request, 'main.html')

def forms_option(request):
	option = str(request.GET.get('forms_opt'))

	if option == 'fill':
		return HttpResponseRedirect('http://127.0.0.1:8000/forms/fill_form/')
	elif option == 'show':
		return HttpResponseRedirect('http://127.0.0.1:8000/forms/show_all/')



def fill_form(request):
	return render(request, 'fill_form.html')


def show_all(request):

	fname = request.GET.get('firstname')
	lname = request.GET.get('lastname')

	if not (fname == None and lname == None):
		dict = {
			'firstname' : fname,
			'lastname' : lname
		}

		new_ele = MyData(firstname = fname, lastname = lname)
		new_ele.save()	


	all_data = MyData.objects.all()

	ctx = {
		'data' : all_data
	}

	return render(request, 'show_all.html', ctx)