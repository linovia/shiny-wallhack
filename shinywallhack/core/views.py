
from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import get_user_model


from .models import Domain
from .forms import RegisterForm


class SignupView(FormView):
    template_name = 'signup.html'
    form_class = RegisterForm
    success_url = reverse_lazy('welcome')

    def form_valid(self, form):
        form.cleaned_data
        user = get_user_model().objects.create(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password'],
        )
        domain = Domain.objects.create(
            domain=form.cleaned_data['domain'],
            user=user,
        )
        return super(SignupView, self).form_valid(form)
