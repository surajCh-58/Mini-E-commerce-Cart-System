from django import forms
from . models import *
class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['name','price','category']
        labels={
            'name':'Enter Name',
            'price':'Enter Price',
            'category':'Enter Category'
        }
        widgets={
            'name':forms.TextInput(attrs={'placeholder':'Enter name'}),
            'price':forms.TextInput(attrs={'placeholder':'Enter price'}),
            'category':forms.Select()
        }
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        common_class="form-control"
        self.fields['category'].empty_label="--select category--"
        for field in self.fields.values():
            field.widget.attrs.update({'class':common_class})
class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['name']

        labels={
            'name':'Enter Category'
        }
        widgets={
            'name':forms.TextInput(attrs={'placeholder':'Enter Category'})
        }

    def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            common_class="form-control"

            for field in self.fields.values():
                field.widget.attrs.update({'class':common_class})
