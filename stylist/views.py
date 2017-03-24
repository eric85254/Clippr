from datetime import datetime

from django.core import serializers
from django.db.models import Q
from django.http import JsonResponse
from django.utils import timezone

from django.shortcuts import render, redirect

from core.models import Appointment, GlobalMenu, ItemInBill, Review
from core.utils.view_logic import UserLogic
from stylist.forms import NewPortfolioHaircutForm, MenuOptionForm
from stylist.models import PortfolioHaircut, StylistMenu, Shift
from stylist.utils.view_logic import BillLogic, StylistLogic


def profile(request):
    if request.user.is_stylist == 'YES':
        full_name = request.user.get_full_name()

        portfolio_haircuts = PortfolioHaircut.objects.filter(stylist=request.user)
        stylist_options = StylistMenu.objects.filter(stylist=request.user)

        return render(request, 'stylist/profile.html',
                      {'full_name': full_name,
                       'stylist': request.user,
                       'portfolio_haircuts': portfolio_haircuts,
                       'stylist_options': stylist_options}, )
    else:
        return redirect('core:logout')


def dashboard(request):
    if request.user.is_stylist == 'YES':
        pending_appointments = Appointment.objects.filter(stylist=request.user,
                                                          status=Appointment.STATUS_PENDING).order_by('-date')
        accepted_appointments = Appointment.objects.filter(stylist=request.user,
                                                           status=Appointment.STATUS_ACCEPTED).order_by('-date')

        completed_appointments = Appointment.objects.filter(stylist=request.user,
                                                            status=Appointment.STATUS_COMPLETED).order_by('-date')

        pending_appointments_bill = BillLogic.combine_appointment_bill(pending_appointments)
        accepted_appointments_bill = BillLogic.combine_appointment_bill(accepted_appointments)
        completed_appointments_bill = BillLogic.combine_appointment_bill(completed_appointments)

        incomplete_reviews = Review.objects.filter(customer_rating__isnull=True)
        complete_reviews = Review.objects.filter(stylist_rating__isnull=False, customer_rating__isnull=False)
        stylist_options = StylistMenu.objects.filter(stylist=request.user)
        return render(request, 'stylist/stylistReal/dashboard/dashboard_core.html',
                      {'full_name': request.user.get_full_name(),
                       # 'pending_appointments': pending_appointments,
                       # 'accepted_appointments': accepted_appointments,
                       # 'completed_appointments': completed_appointments,
                       'pending_appointments_bill': pending_appointments_bill,
                       'accepted_appointments_bill': accepted_appointments_bill,
                       'completed_appointments_bill': completed_appointments_bill,
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
        pending_appointments = Appointment.objects.filter(stylist=request.user,
                                                          status=Appointment.STATUS_PENDING).order_by('-date')
        accepted_appointments = Appointment.objects.filter(stylist=request.user,
                                                           status=Appointment.STATUS_ACCEPTED).order_by('-date')
        declined_appointments = Appointment.objects.filter(stylist=request.user,
                                                           status=Appointment.STATUS_DECLINED).order_by('-date')

        rescheduled_appointments = Appointment.objects.filter(
            (Q(status=Appointment.STATUS_RESCHEDULED_BYCUSTOMER) | Q(status=Appointment.STATUS_RECHEDULED_BYSTYLIST)),
            stylist=request.user).order_by('-date')
        completed_appointments = Appointment.objects.filter(stylist=request.user,
                                                            status=Appointment.STATUS_COMPLETED).order_by('-date')

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

                Review.objects.create(appointment=appointment)
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
                    ItemInBill.objects.create(item_custom=request.POST.get('item_custom'),
                                                     price=request.POST.get('price'), appointment=appointment)

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
                ItemInBill.objects.create(item_portfolio=haircut, price=haircut.price, appointment=appointment)
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
                    ItemInBill.objects.create(item_custom='Travel Fee', price=request.POST.get('travel_fee'),
                                                     appointment=appointment)
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
        stylist_options = StylistMenu.objects.filter(stylist=request.user)

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
                    menu_main = StylistMenu.objects.get(pk=request.POST.get('stylist_option_pk'))
                new_portfolioHaircut.menu_option = menu_main
                new_portfolioHaircut.save()

            return redirect('stylist:profile')
        elif request.method == 'GET':
            stylist_options = StylistMenu.objects.filter(stylist=request.user)
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
                menu_main = StylistMenu.objects.get(pk=request.POST.get('stylist_option_pk'))

            haircut.menu_option = menu_main
            haircut.save()

            return redirect('stylist:profile')

        if request.method == 'GET':
            haircut = PortfolioHaircut.objects.get(pk=request.GET.get('portfoliohaircut_pk'))
            stylist_options = StylistMenu.objects.filter(stylist=request.user)
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
            menu_options = GlobalMenu.objects.all().exclude(modified_global__stylist=request.user)
            stylist_options = StylistMenu.objects.filter(stylist=request.user)
            return render(request, 'stylist/menu/select_menu_option.html',
                          {'menu_options': menu_options, 'stylist_options': stylist_options})

        elif request.method == 'POST':
            global_menu = GlobalMenu.objects.get(pk=request.POST.get('menu_option_pk'))
            stylist_menu = StylistMenu(
                stylist=request.user,
                name=global_menu.name,
                price=global_menu.price,
                duration=global_menu.duration,
                modified_global=global_menu
            )
            stylist_menu.save()
            return redirect('stylist:select_menu_option')
    else:
        return redirect('core:logout')


def remove_menu_option(request):
    if request.user.is_stylist == 'YES':
        if request.method == 'GET':
            return redirect(request.META.get('HTTP_REFERER'))

        if request.method == 'POST':
            stylist_selection = StylistMenu.objects.get(pk=request.POST.get('stylist_option_pk'))
            stylist_selection.delete()
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('core:logout')


# ToDo: difference between select menu_option and create_menu_option??
def create_menu_option(request):
    if request.user.is_stylist == 'YES':
        if request.method == 'POST':
            menu_option_form = MenuOptionForm(request.POST)

            if menu_option_form.is_valid():
                new_option = menu_option_form.save(commit=False)
                new_option.save(commit=False)
                new_option.stylist = request.user
                new_option.save()

                return redirect('stylist:select_menu_option')

        if request.method == 'GET':
            return render(request, 'stylist/menu/create_menu_option.html')
    else:
        return redirect('core:logout')


def edit_menu_option(request):
    if request.user.is_stylist == 'YES':
        if request.method == 'POST':
            stylist_option = StylistMenu.objects.get(pk=request.POST.get('stylist_option_pk'))

            stylist_option.name = request.POST.get('name')
            stylist_option.price = request.POST.get('price')
            stylist_option.stylist = request.user
            stylist_option.save()

            return redirect('stylist:select_menu_option')

        if request.method == 'GET':
            stylist_option = StylistMenu.objects.get(pk=request.GET.get('stylist_option_pk'))
            return render(request, 'stylist/menu/edit_menu_option.html', {'stylist_option': stylist_option})
    else:
        return redirect('core:logout')


def delete_menu_option(request):
    if request.user.is_stylist == 'YES':
        if request.method == 'POST':
            stylist_option = StylistMenu.objects.get(pk=request.POST.get('stylist_option_pk'))
            stylist_option.delete()
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
        stylist_options = StylistMenu.objects.filter(stylist=request.user)

        return render(request, 'stylist/stylistReal/profile/profile_core.html',
                      {'full_name': full_name,
                       'stylist': request.user,
                       'portfolio_haircuts': portfolio_haircuts,
                       'stylist_options': stylist_options}, )
    else:
        return redirect('core:logout')


def render_calendar_page(request):
    return render(request, 'stylist/calendar/calendar_test.html')

