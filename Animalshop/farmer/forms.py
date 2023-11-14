from django import forms
from .models import sell_animal
 
 
class PhotoForm(forms.ModelForm):
 
    class Meta:
        model = sell_animal
        fields = ['animal_id', 'photo']