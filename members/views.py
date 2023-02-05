from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User

class UserRegisterView(generic.CreateView):
    from_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    fields = '__all__'


    def get_queryset(self):
         return User.objects.all()


