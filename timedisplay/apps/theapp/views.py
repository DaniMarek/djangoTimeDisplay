from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from time import gmtime, strftime

def index(request):
	context={
		'time': datetime.now()
	}

	
	return render(request, 'theapp/index.html', context)

