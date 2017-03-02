from datetime import datetime

from django.db.models import Q
from django.utils import timezone

from django.shortcuts import render, redirect

from core.models import Appointment, Menu, ItemInBill, Review
from core.utils.view_logic import UserLogic
from stylist.forms import NewPortfolioHaircutForm, MenuOptionForm
from stylist.models import PortfolioHaircut, StylistBridgeMenu
from stylist.utils.view_logic import BillLogic


def profile(request):
    if request.user.is_stylist == 'YES':
        full_name = request.user.get_full_name()

        portfolio_haircuts = PortfolioHaircut.objects.filter(stylist=request.user)
        stylist_options = StylistBridgeMenu.objects.filter(stylist=request.user)

        return render(request, 'stylist/profile.html',
                      {'full_name': full_name,
                       'stylist': request.user,
                       'portfolio_haircuts': portfolio_haircuts,
                       'stylist_options': stylist_options}, )
    else:
        return redirect('core:logout')


def dashboard(request):
    if request.user.is_stylist == 'YES':
        pending_appointments = Appointment.objects.filter(stylist=request.user, status=Appointment.STATUS_PENDING)
        accepted_appointments = Appointment.objects.filter(stylist=request.user, status=Appointment.STATUS_ACCEPTED)
        declined_appointments = Appointment.objects.filter(stylist=request.user, status=Appointment.STATUS_DECLINED)
        rescheduled_bystylist_appointments = Appointment.objects.filter(stylist=request.user,
                                                                        status=Appointment.STATUS_RECHEDULED_BYSTYLIST)
        rescheduled_bycustomer_appointments = Appointment.objects.filter(stylist=request.user,
                                                                         status=Appointment.STATUS_RESCHEDULED_BYCUSTOMER)
        completed_appointments = Appointment.objects.filter(stylist=request.user, status=Appointment.STATUS_COMPLETED)

        incomplete_reviews = Review.objects.filter(customer_rating__isnull=True)
        complete_reviews = Review.objects.filter(stylist_rating__isnull=False, customer_rating__isnull=False)
        stylist_options = StylistBridgeMenu.objects.filter(stylist=request.user)
        return render(request, 'stylist/stylistReal/dashboard/dashboard_core.html',
                      {'full_name': request.user.get_full_name(),
                       'pending_appointments': pending_appointments,
                       'accepted_appointments': accepted_appointments,
                       'declined_appointments': declined_appointments,
                       'rescheduled_bystylist_appointments': rescheduled_bystylist_appointments,
                       'rescheduled_bycustomer_appointments': rescheduled_bycustomer_appointments,
                       'completed_appointments': completed_appointments,
                       'incomplete_reviews': incomplete_reviews,
                       'complete_reviews': complete_reviews,
                       'stylist_options': stylist_options})
    else:
        return redirect('core:logout')


def transactions(request):
    if request.user.is_stylist == 'YES':
        if request.method == 'GET':
            appointments = Appointment.objects.filter(stylist=request.user, status=Appointment.STATUS_COMPLETED)
            bills = {}
            for appointment in appointments:
                items_in_bill = ItemInBill.objects.filter(appointment=appointment)
                bills[appointment] = items_in_bill

            return render(request, 'stylist/transactions.html', {'bills': bills})
        if request.method == 'POST':
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('core:logout')


'''
    MODIFYING APPOINTMENT & RELATED VIEWS
'''


def appointments(request):
    if request.user.is_stylist == 'YES':
        pending_appointments = Appointment.objects.filter(stylist=request.user, status=Appointment.STATUS_PENDING)
        accepted_appointments = Appointment.objects.filter(stylist=request.user, status=Appointment.STATUS_ACCEPTED)
        declined_appointments = Appointment.objects.filter(stylist=request.user, status=Appointment.STATUS_DECLINED)

        rescheduled_appointments = Appointment.objects.filter((Q(status=Appointment.STATUS_RESCHEDULED_BYCUSTOMER) | Q(status=Appointment.STATUS_RECHEDULED_BYSTYLIST)), stylist=request.user).order_by('-date')
        completed_appointments = Appointment.objects.filter(stylist=request.user, status=Appointment.STATUS_COMPLETED)

        return render(request, 'stylist/stylistReal/stylist_appointments.html',
                      {'full_name': request.user.get_full_name(),
                       'stylist_reschedule': Appointment.STATUS_RECHEDULED_BYSTYLIST,
                       'customer_reschedule': Appointment.STATUS_RESCHEDULED_BYCUSTOMER,
                       'pending_appointments': pending_appointments,
                       'accepted_appointments': accepted_appointments,
                       'declined_appointments': declined_appointments,
                       'rescheduled_appointments': rescheduled_appointments,
                       'completed_appointments': completed_appointments})
    else:
        return redirect('core:logout')


def accept_appointment(request):
    if request.user.is_stylist == 'YES':
        if request.method == 'POST':
            appointment = Appointment.objects.get(pk=request.POST.get('appointment_pk'))
            appointment.status = Appointment.STATUS_ACCEPTED
            appointment.save()
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('core:logout')


def decline_appointment(request):
    if request.user.is_stylist == 'YES':
        if request.method == 'POST':
            appointment = Appointment.objects.get(pk=request.POST.get('appointment_pk'))
            appointment.status = Appointment.STATUS_DECLINED
            appointment.save()
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('core:logout')


def reschedule_appointment(request):
    if request.user.is_stylist == 'YES':
        if request.method == 'POST':
            appointment = Appointment.objects.get(pk=request.POST.get('appointment_pk'))
            appointment.status = Appointment.STATUS_RECHEDULED_BYSTYLIST
            appointment.date = datetime.strptime(request.POST.get('date'), '%Y-%m-%dT%H:%M')
            appointment.save()
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('core:logout')


def complete_appointment(request):
    if request.user.is_stylist == 'YES':
        if request.method == 'POST':
            appointment = Appointment.objects.get(pk=request.POST.get('appointment_pk'))
            if timezone.now() > appointment.date:
                appointment.status = Appointment.STATUS_COMPLETED
                appointment.save()

                review = Review.objects.create(appointment=appointment)
                review.save()
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('core:logout')


'''
    REVIEWS
'''


def submit_review(request):
    if request.user.is_stylist == 'YES':
        if request.method == 'POST':
            review = Review.objects.get(pk=request.POST.get('review_pk'))
            review.customer_rating = int(request.POST.get('rating'))
            review.save()
            UserLogic.update_average(review)
            return redirect('stylist:dashboard')
    else:
        return redirect('core:logout')


'''
    APPOINTMENT / BILL RELATED VIEWS
'''


def view_bill(request):
    if request.user.is_stylist == 'YES':
        if request.method == 'GET':
            appointment = Appointment.objects.get(pk=request.GET.get('appointment_pk'))

            bill = ItemInBill.objects.filter(appointment=appointment)

            request.session['appointment_for_bill'] = request.GET.get('appointment_pk')
            return render(request, 'stylist/bill/view_bill.html', {'bill': bill})
        else:
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('core:logout')


def delete_item(request):
    if request.user.is_stylist == 'YES':
        if request.method == 'POST':
            item = ItemInBill.objects.get(pk=request.POST.get('item_pk'))
            item.delete()

            appointment = Appointment.objects.get(pk=request.session['appointment_for_bill'])
            BillLogic.update_price(appointment)
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('core:logout')


def add_item(request):
    if request.user.is_stylist == 'YES':
        if request.method == 'GET':
            return render(request, 'stylist/bill/add_item_form.html')
        if request.method == 'POST':
            if 'custom' in request.POST:
                appointment = Appointment.objects.get(pk=request.session['appointment_for_bill'])
                if appointment.status is not Appointment.STATUS_COMPLETED:
                    item = ItemInBill.objects.create(item_custom=request.POST.get('item_custom'),
                                                     price=request.POST.get('price'), appointment=appointment)
                    item.save()
                    BillLogic.update_price(appointment)
                return redirect('stylist:dashboard')
        else:
            return redirect('core:logout')
    else:
        return redirect('core:logout')


def add_haircut(request):
    if request.user.is_stylist == 'YES':
        if request.method == 'GET':
            portfolio_haircuts = PortfolioHaircut.objects.filter(stylist=request.user)
            return render(request, 'stylist/bill/add_haircut_toBill.html', {'portfolio_haircuts': portfolio_haircuts})
        if request.method == 'POST':
            haircut = PortfolioHaircut.objects.get(pk=request.POST.get('portfoliohaircut_pk'))
            appointment = Appointment.objects.get(pk=request.session['appointment_for_bill'])
            if appointment.status is not Appointment.STATUS_COMPLETED:
                item = ItemInBill.objects.create(item_portfolio=haircut, price=haircut.price, appointment=appointment)
                item.save()
                BillLogic.update_price(appointment)
            return redirect('stylist:dashboard')
    else:
        return redirect('core:logout')


def add_travel_fee(request):
    if request.user.is_stylist == 'YES':
        if request.method == 'POST':
            appointment = Appointment.objects.get(pk=request.POST.get('appointment_pk'))
            if (appointment.status is not Appointment.STATUS_COMPLETED) and (
                        appointment.status is not Appointment.STATUS_ACCEPTED):
                if ItemInBill.objects.filter(item_custom='Travel Fee', appointment=appointment).exists():
                    item = ItemInBill.objects.get(item_custom='Travel Fee')
                    item.price = request.POST.get('travel_fee')
                else:
                    item = ItemInBill.objects.create(item_custom='Travel Fee', price=request.POST.get('travel_fee'),
                                                     appointment=appointment)
                    item.save()
                appointment.status = Appointment.STATUS_RECHEDULED_BYSTYLIST
                BillLogic.update_price(appointment)
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('core:logout')


'''
    PORTFOLIO HAIRCUT VIEWS
'''


def portfolio(request):
    if request.user.is_stylist == 'YES':
        full_name = request.user.get_full_name()

        portfolio_haircuts = PortfolioHaircut.objects.filter(stylist=request.user)
        stylist_options = StylistBridgeMenu.objects.filter(stylist=request.user)

        return render(request, 'stylist/stylistReal/portfolio/portfolio_core.html',
                      {'full_name': full_name,
                       'stylist': request.user,
                       'portfolio_haircuts': portfolio_haircuts,
                       'stylist_options': stylist_options}, )
    else:
        return redirect('core:logout')


def upload_haircut(request):
    if request.user.is_stylist == 'YES':
        if request.method == 'POST':
            new_portfolioHaircut_form = NewPortfolioHaircutForm(request.POST)

            if new_portfolioHaircut_form.is_valid():
                new_portfolioHaircut = new_portfolioHaircut_form.save(commit=False)
                new_portfolioHaircut.stylist = request.user
                new_portfolioHaircut.picture = request.FILES['picture']
                # Finding and adding selected menu option to new_portfolioHaircut
                if request.POST.get('stylist_option_pk') == 'none':
                    menu_main = None
                else:
                    menu_main = StylistBridgeMenu.objects.get(pk=request.POST.get('stylist_option_pk')).menu_option
                new_portfolioHaircut.menu_option = menu_main
                new_portfolioHaircut.save()

            return redirect('stylist:profile')
        elif request.method == 'GET':
            stylist_options = StylistBridgeMenu.objects.filter(stylist=request.user)
            return render(request, 'stylist/upload_haircut.html', {'stylist_options': stylist_options})

    else:
        return redirect('core:logout')


def edit_portfoliohaircut(request):
    if request.user.is_stylist == 'YES':
        if request.method == 'POST':
            haircut = PortfolioHaircut.objects.get(pk=request.POST.get('portfoliohaircut_pk'))

            if 'picture' in request.FILES:
                haircut.picture = request.FILES['picture']
            haircut.name = request.POST.get('name')
            haircut.description = request.POST.get('description')
            haircut.price = request.POST.get('price')

            if request.POST.get('stylist_option_pk') == 'none':
                menu_main = None
            else:
                menu_main = StylistBridgeMenu.objects.get(pk=request.POST.get('stylist_option_pk')).menu_option

            haircut.menu_option = menu_main
            haircut.save()

            return redirect('stylist:profile')

        if request.method == 'GET':
            haircut = PortfolioHaircut.objects.get(pk=request.GET.get('portfoliohaircut_pk'))
            stylist_options = StylistBridgeMenu.objects.filter(stylist=request.user)
            return render(request, 'stylist/edit_portfoliohaircut.html',
                          {'haircut': haircut, 'stylist_options': stylist_options})
    else:
        return redirect('core:logout')


def delete_portfoliohaircut(request):
    if request.user.is_stylist == 'YES':
        if request.method == 'POST':
            haircut = PortfolioHaircut.objects.get(pk=request.POST.get('portfolio_haircut_pk'))
            haircut.delete()

        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('core:logout')


'''
    MENU OPTION
'''


def select_menu_option(request):
    if request.user.is_stylist == 'YES':
        if request.method == 'GET':
            menu_options = Menu.objects.all().exclude(stylistbridgemenu__stylist=request.user)
            stylist_options = StylistBridgeMenu.objects.filter(stylist=request.user)
            return render(request, 'stylist/menu/select_menu_option.html',
                          {'menu_options': menu_options, 'stylist_options': stylist_options, 'creator_stylist': Menu.STYLIST})

        elif request.method == 'POST':
            menu_option = Menu.objects.get(pk=request.POST.get('menu_option_pk'))
            stylist_selection = StylistBridgeMenu.objects.create(stylist=request.user, menu_option=menu_option)
            stylist_selection.save()
            return redirect('stylist:select_menu_option')
    else:
        return redirect('core:logout')


def remove_menu_option(request):
    if request.user.is_stylist == 'YES':
        if request.method == 'GET':
            return redirect(request.META.get('HTTP_REFERER'))

        if request.method == 'POST':
            stylist_selection = StylistBridgeMenu.objects.get(pk=request.POST.get('stylist_option_pk'))
            stylist_selection.delete()
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('core:logout')


def create_menu_option(request):
    if request.user.is_stylist == 'YES':
        if request.method == 'POST':
            menu_option_form = MenuOptionForm(request.POST)

            if menu_option_form.is_valid():
                new_option = menu_option_form.save(commit=False)

                if 'picture' in request.FILES:
                    new_option.picture = request.FILES.get('picture')
                new_option.creator = Menu.STYLIST
                new_option.save()

                StylistBridgeMenu.objects.create(stylist=request.user, menu_option=new_option,
                                                 price=request.POST.get('price'))

                return redirect('stylist:select_menu_option')

        if request.method == 'GET':
            return render(request, 'stylist/menu/create_menu_option.html')
    else:
        return redirect('core:logout')


def edit_menu_option(request):
    if request.user.is_stylist == 'YES':
        if request.method == 'POST':
            stylist_option = StylistBridgeMenu.objects.get(pk=request.POST.get('stylist_option_pk'))
            stylist_option.price = request.POST.get('price')
            if 'picture' in request.FILES:
                picture = request.FILES.get('picture')
            else:
                picture = None

            if stylist_option.menu_option.creator == Menu.STYLIST:
                stylist_option.menu_option.name = request.POST.get('name')
                stylist_option.menu_option.description = request.POST.get('description')
                stylist_option.menu_option.picture = picture
                stylist_option.menu_option.save()

            else:
                StylistBridgeMenu.objects.get(pk=request.POST.get('stylist_option_pk')).delete()
                menu_option = Menu(
                    creator=Menu.STYLIST,
                    name=request.POST.get('name'),
                    picture=picture,
                    description=request.POST.get('description')
                )
                menu_option.save()
                StylistBridgeMenu.objects.create(
                    stylist=request.user,
                    menu_option=menu_option,
                    price=request.POST.get('price')
                )
            return redirect('stylist:select_menu_option')

        if request.method == 'GET':
            stylist_option = StylistBridgeMenu.objects.get(pk=request.GET.get('stylist_option_pk'))
            return render(request, 'stylist/menu/edit_menu_option.html', {'stylist_option': stylist_option})
    else:
        return redirect('core:logout')


def delete_menu_option(request):
    if request.user.is_stylist == 'YES':
        if request.method == 'POST':
            stylist_option = StylistBridgeMenu.objects.get(pk=request.POST.get('stylist_option_pk'))
            stylist_option.menu_option.delete()
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('core:logout')


'''
    NEW DEVELOPMENT
'''


def profile_test(request):
    if request.user.is_stylist == 'YES':
        full_name = request.user.get_full_name()

        portfolio_haircuts = PortfolioHaircut.objects.filter(stylist=request.user)
        stylist_options = StylistBridgeMenu.objects.filter(stylist=request.user)

        return render(request, 'stylist/stylistReal/profile/profile_core.html',
                      {'full_name': full_name,
                       'stylist': request.user,
                       'portfolio_haircuts': portfolio_haircuts,
                       'stylist_options': stylist_options}, )
    else:
        return redirect('core:logout')
