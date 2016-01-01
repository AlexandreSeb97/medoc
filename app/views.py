"""
Definition of views.
"""
from django.http import Http404
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.models import Doctor
from app.models import Hospital
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from app.forms import RegisterForm, LoginForm, UserChangeForm
from app.models import MyDoctor

def hospital(request):
    """ Afficher tous les hopitaux de notre blog """
    hospital = Hospital.objects.all()
    """Renders the hospital page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/hospitals.html',
	{'hospitals': hospital},
        context_instance = RequestContext(request,
        {
            'title':'Hospitals',
			'message':'List of all Hospitals in MeDOC',
            'year':datetime.now().year,
        })
    )

def medoc(request):
   """ Afficher tous les medecins de notre database """
   doctor = Doctor.objects.all()
   return render(request, 'app/medoc.html', {'doctors': doctor})
   """Renders the medoc page."""
   assert isinstance(request, HttpRequest)
   return render(
       request,
       'app/medoc.html',
       context_instance = RequestContext(request,
       {
           'title':'Medoc',
           'message':'How do you feel today?',
           'year':datetime.now().year,
       })
   )

def hospital_fr(request):
    """ Afficher tous les hopitaux de notre blog """
    hospital = Hospital.objects.all()
    return render(request, 'app/fr/hospitals_fr.html', {'hospitals': hospital})
    """Renders the hospital page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/fr/hospitals_fr.html',
        context_instance = RequestContext(request,
        {
            'title':'Hospitaux',
			'message':'List of all Hospitals in MeDOC',
            'year':datetime.now().year,
        })
    )

def hospital_kr(request):
    """ Afficher tous les hopitaux de notre blog """
    hospital = Hospital.objects.all()
    return render(request, 'app/kr/hospitals_kr.html', {'hospitals': hospital})
    """Renders the hospital page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/kr/hospitals_kr.html',
        context_instance = RequestContext(request,
        {
            'title':'Lopital',
			'message':'List of all Hospitals in MeDOC',
            'year':datetime.now().year,
        })
    )

def info(request, id):
	"""Renders full hospital infos."""
	try:
		hospital = Hospital.objects.get(id=id)
	except Hospital.DoesNotExist:
		raise Http404
	return render(request, 'blog/info.html', {'hospitals': hospital})


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Language',
            'year':datetime.now().year,
			'date':datetime.now().date,
        })
    )

def _en(request):
    """Renders english home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/page_en.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
			'date':datetime.now(),
        })
    )

def _fr(request):
    """Renders french home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/fr/page_fr.html',
        context_instance = RequestContext(request,
        {
            'title':"Page d'accueil",
            'year':datetime.now().year,
			'date':datetime.now(),
        })
    )

def _kr(request):
	"""Renders creole home page."""
	assert isinstance(request, HttpRequest)
	return render(
		request,
		'app/kr/page_kr.html',
		context_instance = RequestContext(request,
		{
			'title':'Paj Akey',
			'year':datetime.now().year,
			'date':datetime.now(),
		})
	)


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Who are we?',
            'message':'Learn about the men behind MeDOC and SHARPRISE',
            'year':datetime.now().year,
        })
    )

def contact_kr(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/kr/contact_kr.html',
        context_instance = RequestContext(request,
        {
            'title':'Kontak',
            'message':"App lan ap baw edek? Kontakte n'!",
            'year':datetime.now().year,
        })
    )

def contact_fr(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/fr/contact_fr.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':"L'app vous pose des problemes? Contactez nous!",
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':"What's up Doc?",
            'year':datetime.now().year,
        })
    )

def about_kr(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/kr/about_kr.html',
        context_instance = RequestContext(request,
        {
            'title':'A Pwopo',
            'message':"Sa k'ap fet Doc la?",
            'year':datetime.now().year,
        })
    )

def about_fr(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/fr/about_fr.html',
        context_instance = RequestContext(request,
        {
            'title':'A Propos',
            'message':"Bonjour Doc!",
            'year':datetime.now().year,
        })
    )

def _head(request):
	""" Afficher tous les medecins de notre database """
	mydoctor = MyDoctor.objects.all()
	"""Renders the medoc page."""
	assert isinstance(request, HttpRequest)
	return render(
		request,
		'app/head.html',
		{'mydoctors': mydoctor},
		context_instance = RequestContext(request,
		{
			'title':'Registered Docs',
			'message':"Docs registered with us and ready to serve you!",
            'todocs': "Are you doctor and aren't registed yet? Click on the button below!",
			'year':datetime.now().year,
		})
	)

def medoc_kr(request):
    """Renders the app page"""
    assert isinstance(request, HttpRequest)
    return render(
       request,
       'app/kr/medoc_kr.html',
       context_instance = RequestContext(request,
        {
            'title':'Medoc',
            'message':"Koman w' santi w' jodia?",
            'year':datetime.now().year,
        })
    )

def medoc_fr(request):
    """Renders the app page"""
    assert isinstance(request, HttpRequest)
    return render(
       request,
       'app/fr/medoc_fr.html',
       context_instance = RequestContext(request,
        {
            'title':'Medoc',
            'message':"Comment vous sentez vous aujourd'hui?",
            'year':datetime.now().year,
        })
    )

def head_kr(request):
	""" Afficher tous les medecins de notre database """
	doctor = Doctor.objects.all()
	"""Renders the medoc page."""
	assert isinstance(request, HttpRequest)
	return render(
		request,
		'app/kr/head_kr.html',
		{'doctors': doctor},
		context_instance = RequestContext(request,
		{
			'title':'Dokte an Ayiti',
			'message':'Koman w santi w jodia',
			'year':datetime.now().year,
		})
	)

def head_fr(request):
	""" Afficher tous les medecins de notre database """
	doctor = Doctor.objects.all()
	"""Renders the medoc page."""
	assert isinstance(request, HttpRequest)
	return render(
		request,
		'app/fr/head_fr.html',
		{'doctors': doctor},
		context_instance = RequestContext(request,
		{
			'title':'Medecins en Haiti',
			'message':'Comment vous sentez vous aujourdhui?',
			'year':datetime.now().year,
		})
	)

def auth_login(request):
	form = LoginForm(request.POST or None)
	next_url = request.GET.get('next')
	if form.is_valid():
		name = form.cleaned_data['name']
		password = form.cleaned_data['password']
		user = authenticate(name=name, password=password)
		if user is not None:
			login(request, user)
			if next_url is not None:
				return HttpResponseRedirect(next_url)
			return HttpResponseRedirect("/create")
	action_url = reverse("login")
	title = "Login"
	submit_btn = title
	submit_btn_class = "btn-success btn-block"
	context = {
		"form": form,
		"action_url": action_url,
		"title": 'Log in',
		"submit_btn": submit_btn,
		"submit_btn_class": submit_btn_class,
		}
	return render(request, "app/account/account_login.html", context)

def auth_register(request):

	form = RegisterForm(request.POST or None)
	if form.is_valid():
		name = form.cleaned_data['name']
		country = form.cleaned_data['country']
		specialite = form.cleaned_data['specialite']
		email = form.cleaned_data['email']
		password = form.cleaned_data['password2']
		#MyUser.objects.create_user(name=name, email=email, password=password, country=country, specialite=specialite)
		new_user = MyDoctor()
		new_user.name = name
		new_user.email = email
		new_user.country = country
		new_user.specialite = specialite
		#new_user.password = password #WRONG
		new_user.set_password(password) #RIGHT
		new_user.save()

	action_url = reverse("register")
	title = "Register"
	submit_btn = "Create free account"

	context = {
		"form": form,
		"action_url": action_url,
		"title": 'Register now!',
		"submit_btn": submit_btn
		}
	return render(request, "app/account/account_register.html", context)
