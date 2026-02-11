from django import forms
from .models import World
from .models import PoliticalEntity

class WorldForm(forms.ModelForm):
    class Meta:
        model = World
        fields = ["seed", "name", "description"]


class PoliticalEntityForm(forms.ModelForm):
    class Meta:
        model = PoliticalEntity
        fields = [
            "name",
            "government_type",
            "dominant_trait",
            "power_level",
            "description",
        ]
