from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from .models import *
from .forms import AddUserForm

# from django.contrib import messages
# # from django.views.generic.list import ListView
# from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
# from .forms import AddUserForm, AddCollaboraterForm, AddFieldForm, AddCompetenceForm, AddCertificationForm, AddSocietyForm, ProfilForm, ModifyProfilForm, AddCompCollabForm, AddSocietyForm, ProfilFormUser
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import update_session_auth_hash
# from django.contrib.auth.views import PasswordChangeView
# from django.urls import reverse_lazy
# class UserList(ListView):
  
#     # specify the model for list view
#     model = User
#     template_name = 'User_List.html'
    
def index(request):
    # users = User.objects.all()
    # context = { 'users':users}
    template = loader.get_template('app/index.html')
    return HttpResponse(template.render({}, request))

def register(request):
    form = AddUserForm()
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = form.save()
            messages.success(request,f'Bienvenue {username}, votre compte a été crée avec succés')
            return render(request, 'register.html', context)
            # return redirect('matrice:Liste_des_utilisateurs')
        else:
            messages.error(request, "Vous avez déjà un compte")
    else:
        form = AddUserForm()
    return render(request, 'register.html', context)
