from django import forms
from .models import Pictures
from django.core.exceptions import ValidationError


class PictureForm(forms.ModelForm):

    class Meta:
        fields = ('name',)
        model = Pictures

    def validate_name(value):
        if not value:
            raise ValidationError('String field cannot be empty.')
