from django import template

from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Div
from crispy_forms.bootstrap import StrictButton, InlineField

from shinywallhack.core.forms import RegisterForm


register = template.Library()


inline_helper = FormHelper()
inline_helper.form_class = 'form-inline'
# helper.field_template = 'bootstrap3/layout/inline_field.html'
inline_helper.layout = Layout(
    InlineField('email', wrapper_class='col-md-3'),
    InlineField('password', wrapper_class='col-md-3'),
    InlineField('domain', wrapper_class='col-md-3'),
    Div(
        StrictButton('Sign in', css_class='btn-large btn-primary', style='width: 100%;'),
        css_class='form-group col-md-3'
    )
)


@register.simple_tag(takes_context=True)
def register_form(context):
    form = RegisterForm()
    form.helper = helper
    form.inline_helper = inline_helper
    context['registration_form'] = form
    return ''
