
from django import forms
from django.contrib.auth import get_user_model
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Submit
from .models import Domain


helper = FormHelper()
helper.add_input(Submit('submit', 'Sign in',
    css_class='btn-large btn-primary', style='width: 100%;'))
helper.layout = Layout(
    'email',
    'password',
    'domain',
    # Submit('Sign in', css_class='btn-large btn-primary'),
)


class RegisterForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    domain = forms.CharField()

    helper = helper

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")
        return email

    def clean_domain(self):
        domain = self.cleaned_data['domain']
        if Domain.objects.filter(domain=domain).exists():
            raise forms.ValidationError("Domain already used.")
        return domain
