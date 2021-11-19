#import requests
from django.shortcuts import render
from UserAccounts.forms import UserForm,UserProfileInfoForm

from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,'UserAccounts/index.html')

@login_required
def special(request):
    # Remember to also set login url in settings.py!
    # LOGIN_URL = '/basic_app/user_login/'
    return HttpResponse("You are logged in. Nice!")

def signup(request):

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_data=request.POST
        user_form = UserForm(user_data)
        profile_form = UserProfileInfoForm(user_data)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            phone=request.POST['phone_number']

            url = "http://2factor.in/API/V1/35d17aec-de95-11e8-a895-0200cd936042/SMS/" + phone + "/AUTOGEN/OTPSEND"
            response = requests.request("GET", url)

            data = response.json()
            request.session['otp_session_data'] = data['Details']
            request.session['user_data'] = user_data
            profile = profile_form.save(commit=False)
            profile.profile_pic = request.FILES['profile_pic']
            request.session['profile_pic'] = profile.filename
            return render(request,'UserAccounts/otp_request.html')
        else:
                    # One of the forms was invalid if this else gets called.
                    print(user_form.errors,profile_form.errors)

    else:
                # Was not an HTTP post so we just render the forms as blank.
                user_form = UserForm()
                profile_form = UserProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'UserAccounts/signup.html',
                                    {'user_form':user_form,
                                   'profile_form':profile_form })

def otp_request(request):

    registered = False
    if request.method == 'POST':
        #calling function for authenticate
        otp = request.POST['otp_field']

        url = "http://2factor.in/API/V1/35d17aec-de95-11e8-a895-0200cd936042/SMS/VERIFY/"+request.session['otp_session_data']+"/"+otp+""
        response = requests.request("GET", url)
        data = response.json()



        if data['Details']=="OTP Matched":

            user_form = UserForm(request.session['user_data'])
            profile_form = UserProfileInfoForm(request.session['user_data'])
            #Save User Form to Database
            user = user_form.save()
            # Hash the password
            user.set_password(user.password)
            # Update with Hashed password
            user.save()
            # Now we deal with the extra info!
            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)

            profile.profile_pic = request.session['profile_pic']
            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user

            print('USER SAVED')

            profile.save()

            registered = True
        else:
            registered = False
    return render(request,'UserAccounts/otp_request.html',{'registered':registered})


def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('home'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'UserAccounts/login.html', {})
