from django import template
from django import forms

from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Field, Div
from crispy_forms.bootstrap import StrictButton, InlineField


register = template.Library()


helper = FormHelper()
helper.form_class = 'form-inline'
# helper.field_template = 'bootstrap3/layout/inline_field.html'
helper.layout = Layout(
    InlineField('email', wrapper_class='col-md-3'),
    InlineField('password', wrapper_class='col-md-3'),
    InlineField('domain', wrapper_class='col-md-3'),
    Div(
        StrictButton('Sign in', css_class='btn-large btn-primary', style='width: 100%;'),
        css_class='form-group col-md-3'
    )
)


class RegisterForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    domain = forms.CharField()

    helper = helper


@register.simple_tag(takes_context=True)
def register_form(context):
    context['registration_form'] = RegisterForm()
    return ''
