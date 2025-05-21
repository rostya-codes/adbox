from django import forms

from ads.models import Ad


class BaseAdForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.__class__.__name__ == 'Select':
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Ad
        fields = ('title', 'description', 'image', 'price', 'category')


class CreateAdForm(BaseAdForm):
    pass


class UpdateAdForm(BaseAdForm):
    pass
