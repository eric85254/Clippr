from django.shortcuts import render


def profile(request):
    full_name = request.user.get_full_name()
    if request.user.customer.customer_picture is not None:
        customer = request.user.customer
    else:
        customer = None
    return render(request, 'customer/profile.html',
                  {'full_name': full_name,
                   'customer': customer})


def dashboard(request):
    return render(request, 'customer/dashboard.html', {'full_name': request.user.get_full_name()})
