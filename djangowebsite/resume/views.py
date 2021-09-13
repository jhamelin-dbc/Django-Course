from django.shortcuts import render


def home(request):
	return render(request, 'home.html', {})

def about(request):
	return render(request, 'about.html', dict_1)

dict_1 = {'first_name':'Jonathan', 'last_name':'Hamelin'}