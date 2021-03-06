from django.shortcuts import render_to_response

from film.models import Film
from login.models import EndUser
from ticket.models import Ticket
from hall.models import Hall
from django.db.models import Q
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib.auth.models import User

from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required,user_passes_test
import datetime
from datetime import timedelta

now=datetime.datetime.now()
curr_date=now.date()
curr_time=now.time()
curr_hour=now.hour

date=datetime.datetime.combine(curr_date,curr_time)

@login_required
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def view_film(request):
	#return HttpResponse(date)
	
	return render_to_response( 'view_film.html',{ "film_list": Film.objects.filter(show_timing__gte=curr_time ) },context_instance=RequestContext(request) )



@login_required
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def selected_film(request):
	filmid=request.GET.get('filmid','')
	return render_to_response('selected_film.html',{"film": Film.objects.get(film_id__exact=filmid) },context_instance=RequestContext(request))	



@login_required
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def get_ticket(request):
	filmid=request.GET.get('filmid','')
	tickets=long(request.POST['number_of_tickets'])	
	film=Film.objects.get(film_id__exact=filmid)
	hallid=film.hall_id
	
	film_hall=Hall.objects.get(hall_id__exact=hallid)
	total_seats=film_hall.total_seats	
	seats_allocated=film_hall.total_seats_allocated

	seats_available=total_seats - seats_allocated
	amount_payable=tickets*film.ticket_charge

	user=User.objects.get(username__exact=request.user)
	enduser=EndUser.objects.using('remote').get(user_id__exact=user.id)

	if(enduser.credits < amount_payable):
		return render_to_response('no_credits.html',{"film": Film.objects.get(film_id__exact=filmid) },context_instance=RequestContext(request))	
	
	if(seats_available<tickets):
		return render_to_response('no_seats.html',{"film": Film.objects.get(film_id__exact=filmid) },context_instance=RequestContext(request))	

	else:
		film_hall.total_seats_allocated +=tickets
		film_hall.save()

		enduser.credits-=amount_payable
		enduser.save(using='remote')
		ticket=Ticket(film_name=film.film_name,end_user=request.user,purchase_datetime=now,ticket_amount=amount_payable)
		ticket.save()
		return render_to_response('download_ticket.html',{"film":film,"filmid":filmid,"user":user.id,"date":now,"amount":amount_payable, 'credits':amount_payable, 'remain':enduser.credits},context_instance=RequestContext(request))	


		
	

		
		

