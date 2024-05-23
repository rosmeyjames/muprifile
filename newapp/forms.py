from django import forms
from .models import profile,portfolio,project
class profileform(forms.ModelForm):
     class Meta:
         model=profile
#         fields=['']
         fields='__all__'


class portfolioform(forms.ModelForm):
    class Meta:
        model=portfolio
        #         fields=['']
        fields='__all__'


class projectform(forms.ModelForm):
    class Meta:
        model=project
        #         fields=['']
        fields='__all__'
