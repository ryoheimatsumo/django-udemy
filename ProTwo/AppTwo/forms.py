from django import forms
from django.core import validators
from AppTwo.models import User


# class FormName(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     varify_email = forms.EmailField(label='ENTER YOUR EMAIL AGAIN')
#     text = forms.CharField(widget=forms.Textarea)
#
#     def clean(self):
#         all_clean_data = super().clean()
#         email = all_clean_data['email']
#         vmail = all_clean_data['varify_email']
#
#         if email != vmail:
#             raise forms.ValidationError("MAKE SURE EMAIL MATCH!")


class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
