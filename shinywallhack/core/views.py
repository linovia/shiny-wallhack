
from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy
from .forms import RegisterForm


class SignupView(FormView):
    template_name = 'signup.html'
    form_class = RegisterForm
    success_url = reverse_lazy('welcome')

    def form_valid(self, form):
        print form.cleaned_data
        return super(SignupView, self).form_valid(form)
