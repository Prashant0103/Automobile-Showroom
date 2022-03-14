from django import forms
from .models import Customer,car,contact

class uform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())    
    class Meta():
        model = Customer
        fields = ('Id','Name','email','username','Age','City','password')


class cform(forms.ModelForm):
    class Meta():
        model = car
        fields = '__all__'
        
class cont(forms.ModelForm):
    class Meta():
        model = contact
        fields = '__all__'
        
