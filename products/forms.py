from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(
        label='Title', 
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your Title",

            }
        )
        )
    email = forms.EmailField()
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Your Description",
                "class": "new-class",
                "rows": 10
            }
        )
        )
    price = forms.DecimalField()

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')

        if not "jc" in title:
            raise forms.ValidationError("This is not a valid title")
        else:
            return title
        
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')

        if not email.endswith(".com"):
            raise forms.ValidationError("This is not a valid email")
        else:
            return email
            


class RawProductForm(forms.Form):
    title = forms.CharField(
        label='Title', 
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your Title",

            }
        )
        )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Your Description",
                "class": "new-class",
                "rows": 10
            }
        )
        )
    price = forms.DecimalField()