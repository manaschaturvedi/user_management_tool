from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class AddUpdateForm(forms.Form):
	first_name = forms.CharField()
	last_name = forms.CharField()
	email = forms.EmailField()
	mobile = forms.CharField(max_length=15)
	age = forms.IntegerField()
	dob = forms.DateField(widget=forms.TextInput(attrs=
                                {
                                    'class':'datepicker'
                                }))
	location = forms.CharField()

	helper = FormHelper()
	helper.add_input(Submit('add-update-user-button', 'Add', css_class='btn-primary'))
	helper.form_method = 'POST'