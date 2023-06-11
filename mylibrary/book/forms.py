from django import forms

from .models import Book

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'


class NewBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('category', 'name', 'description', 'price', 'image',)

        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }


class EditBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'description', 'price', 'image',)

        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }
