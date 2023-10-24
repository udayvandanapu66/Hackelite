#importing thr render,redirect,messages and login required decorator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import Fuelxpress_UserRegisterForm, Fuelxpress_UserUpdateForm, Fuelxpress_ProfileUpdateForm


def register(FE_request):
# instantiate form with request data
    if FE_request.method == 'POST':
# if info is correct, save the form and fetch username
        form = Fuelxpress_UserRegisterForm(FE_request.POST)
        if form.is_valid():
            form.save()
            FE_username = form.cleaned_data.get('username')
#Display the success message
            messages.success(FE_request, f'Your account has been created with Fuelxpress!')
            return redirect('login')
#instantiate the blank form
    else:
        form = Fuelxpress_UserRegisterForm()
    return render(FE_request, 'users/register.html', {'form': form})

#view for profile login, instantiate user and profile updated forms by POST
@login_required
def profile(FE_request):
    if FE_request.method == 'POST':
        FE_uform = Fuelxpress_UserUpdateForm(FE_request.POST, instance=FE_request.user)
        FE_pform = Fuelxpress_ProfileUpdateForm(FE_request.POST,
                                   FE_request.FILES,
                                   instance=FE_request.user.profile)
        if FE_uform.is_valid() and FE_pform.is_valid():
            FE_uform.save()
            FE_pform.save()
            messages.success(FE_request, f'Your account has been updated!')
            return redirect('profile')

    else:
        FE_uform = Fuelxpress_UserUpdateForm(instance=FE_request.user)
        FE_pform = Fuelxpress_ProfileUpdateForm(instance=FE_request.user.profile)
#Creating the context and render template
    context = {
        'u_form': FE_uform,
        'p_form': FE_uform
    }

    return render(FE_request, 'users/profile.html', context)
