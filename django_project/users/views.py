from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, UserExtensionForm, StudentExtensionForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        ext_form = UserExtensionForm(request.POST)
        stud_ext_form = StudentExtensionForm(request.POST)
        if form.is_valid() and ext_form.is_valid() :
            user = form.save()
            ext = ext_form.save(commit=False)
            ext.user = user
            ext.save()
            username = form.cleaned_data.get('username')
            tag = ext_form.cleaned_data.get('tag')
            if tag == "student" and stud_ext_form.is_valid():
                stud_ext = stud_ext_form.save(commit=False)
                stud_ext.user = user
                stud_ext.save()
            messages.success(request, f'Your account has been created! You can login now')
            return redirect('login')
    else:
        form = UserRegisterForm()
        ext_form = UserExtensionForm()
        stud_ext_form = StudentExtensionForm()
    return render(request, 'users/register.html', {'form': form, 'ext_form': ext_form, 'stud_ext_form': stud_ext_form})

#decorator
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been Updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
            'u_form': u_form,
            'p_form': p_form
            }
    return render(request, 'users/profile.html', context)
