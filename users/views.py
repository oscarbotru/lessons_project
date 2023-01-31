from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView
from django.contrib.auth.forms import Form
from users.forms import CustomEditUserForm
from users.models import User


class CustomLoginView(LoginView):
    template_name = 'users/login.html'


class CustomRegisterView(CreateView):
    model = User
    form_class = UserCreationForm

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
            self.object.is_active = False
            send_register_mail()
            self.object.save()
        return super().form_valid(form)


class UserEditProfileView(UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = CustomEditUserForm
    success_url = reverse_lazy('funny:home')

    def get_object(self, queryset=None):
        return self.request.user
