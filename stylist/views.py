from django.shortcuts import render

def profile(request):
	full_name = request.user.get_full_name()
	render(request, 'stylist/profile.html', {'full_name': full_name})
