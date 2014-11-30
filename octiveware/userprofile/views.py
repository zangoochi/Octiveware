from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login

#1rst following view def will be deleted once login and session is in place
def tempIndex(request):
	return render(request, 'userprofile/index.html', {})

def index(request, userName):
	user = request.user
	return render(request, 'userprofile/index.html', {'user': user, })



