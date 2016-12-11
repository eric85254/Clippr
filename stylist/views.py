from django.shortcuts import render


def profile(request):
	full_name = request.user.get_full_name()
	if request.user.profile_picture is not None:
		stylist = request.user.stylist
	else:
		stylist = None
	return render(request, 'stylist/profile.html',
				  {'full_name': full_name,
				   'stylist': stylist})


def dashboard(request):
	return render(request, 'stylist/dashboard.html', {'full_name': request.user.get_full_name()})

