from django.shortcuts import render



def home(request):
	"""
	render the home page
	"""
	context = {}
	return render(request, 'home.html', context)