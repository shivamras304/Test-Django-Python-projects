from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# def main_page(request):
# 	return render(request, 'main_page.html')

def main_page(request):

	html = """<html>
	<head>
		<title>Practice Projects</title>
		<style>
			body {
				background-color: silver;
			}
		</style>
	</head>
	<body>

	<form action="http://127.0.0.1:8000/launch_selected_app" method="get" name="select_app">
		<input type="radio" name="forms_app" value="forms" checked>Forms Project<br>
		<input type="submit" name="submit">
	</body>
	</html>
	"""
	return HttpResponse(html)

def launch_app(request):
	app = str(request.GET.get('forms_app')) 

	if app == 'forms':
		return HttpResponseRedirect('http://127.0.0.1:8000/forms/')
	
	
