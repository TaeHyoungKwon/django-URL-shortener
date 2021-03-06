from django import forms

from .validation import validate_url, validate_first_essential_part

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

class CreateShortenURLForm(forms.Form):
    '''
    * You can be input origin_url by some user
    * Form class can manage input url by validators
    * crispy_forms is third-party app get prettier html form.
    '''
    origin_url = forms.CharField(
        label="", 
        validators=[validate_url, validate_first_essential_part]
    )
    
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Go Shorten', 'Go Shorten', css_class='btnsubmit btn btn-lg btn-default'))
    helper.layout = Layout(
        Field('origin_url',value="http://" ,css_id='inputDefault',css_class='input_size')
    )