from django.shortcuts import render
from django.http import HttpResponseRedirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username=="Ramkishan" and password=="Rathi@143":                
            request.session['is_logged_in'] = True
            return HttpResponseRedirect('index/')
        else:
            return render(request, 'login.html')
    
    return render(request, 'login.html')

def index_view(request):
    if not request.session.get('is_logged_in'):
        return HttpResponseRedirect('login/')
    return render(request, 'index.html')
