from django import forms

from ads.models import Ad


class CreateAdForm(forms.ModelForm):

    class Meta:
        model = Ad
        fields = ('title', 'description', 'image', 'price', 'category')
