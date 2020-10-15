from django import forms
from .validators import url_validator, dot_com_validator

class SubmitURLForm(forms.Form):
    url = forms.CharField(label="Enter URL", validators=[url_validator, dot_com_validator])

    # def clean(self):
    '''
    clean method that cleans the whole form i.e SubmitURLForm
    '''
    #     cleaned_data = super(SubmitURLForm, self).clean()
    #     url =  cleaned_data.get('url')
    #     print('Cleaned Data: ', cleaned_data)
    #     print('URL after .get :', url)
    #     url_validator = URLValidator()
    #     try:
    #         url_validator(url)
    #     except Exception as e:
    #         raise forms.ValidationError('The entered URL is incorrect')
    #     return url

    # def clean_url(self):
    '''
    clean method for cleaning the name of the field in the form, i.e url
    '''
    #     url = self.cleaned_data['url']
    #     url_validator = URLValidator()
    #     try:
    #         url_validator(url)
    #     except Exception as e:
    #         raise forms.ValidationError('The Url entered is not Valid')
    #     return url
