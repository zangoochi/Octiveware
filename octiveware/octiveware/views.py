from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.core.urlresolvers import reverse



def index(request):
	user = request.user
	if user.is_authenticated():
		return redirect(reverse(workFlow, args=[user.username]))
	else:
		return redirect('/login/')

def workFlow(request, userName):
	user = request.user
	if user.is_authenticated():		
		
		return render(request, 'home/workflow.html', {'user': user,})										
