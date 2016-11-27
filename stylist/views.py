from django.shortcuts import render

def profile(request):
	full_name = request.user.get_full_name()
	return render(request, 'stylist/profile.html', {'full_name': full_name})

def dashboard(request):
	return render(request, 'stylist/dashboard.html', {'full_name': request.user.get_full_name()})