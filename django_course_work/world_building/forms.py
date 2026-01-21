from django import forms
from .models import World

class WorldForm(forms.ModelForm):
    class Meta:
        model = World
        fields = ["seed", "name", "description"]
