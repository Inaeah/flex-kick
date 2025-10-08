from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "category", "thumbnail", "is_featured", "brand", "price"]
    
    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_brand(self):
        brand = self.cleaned_data["brand"]
        return strip_tags(brand)
    
    def clean_description(self):
        descrption = self.cleaned_data["descrption"]
        return strip_tags(descrption)
