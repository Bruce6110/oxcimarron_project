from django import forms


class ResortForm(forms.ModelForm):
   

    class Meta:
        exclude = ('id',)
        widgets = {
            'resort_name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.FileInput(attrs={'class': 'form-control'}),
            'skiable_acres': forms.TextInput(attrs={'class': 'form-control'}),
            'base_elevation': forms.NumberInput(attrs={'class': 'form-control'}),
            'vertical_feet': forms.NumberInput(attrs={'class': 'form-control'}),
            'longest_run': forms.NumberInput(attrs={'class': 'form-control'}),
            'personal_rating': forms.TextInput(attrs={'class': 'form-control'}),

        }
