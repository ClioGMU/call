from django_countries.fields import CountryField

class CustomForm(forms.Form):
    country = CountryField().formfield()