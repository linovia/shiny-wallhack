
from django import forms
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Submit


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
