from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttResponseRedirect
from .forms import SubscriberForm
# Create your views here.

def SubscriberForm(request, template='subscriber/subscriber_new.html'):
    if request.method == 'POST':
        form = SubscriberForm(request.Post)
        if form.is_valid():
            # Unpack form values
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            #Create user record
            user = User(username=username, email=email)
            user.set_password(password)
            user.save()


            return HttResponseRedirect('/success')

    else:
        form = SubscriberForm()

    return render(request, template, {'form':form})
