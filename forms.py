from django import forms
from .models import Input, Diseases, DISEASES

# abc: we only need one form to select the states. This form is "conected" in home/display_table
class InputForm(forms.ModelForm):

    disease = forms.ChoiceField(choices=DISEASES, required=True,
                              widget=forms.Select())

    attrs = {'class ' : 'form-nav-control',
             'onchange ' : 'this.form.submit()'}

    class Meta:

        model = Input
        fields = ['disease']


class DiseasesForm(forms.ModelForm):

    attrs = {'class ' : 'form-nav-control',
             'onchange ' : 'this.form.submit()'}

    disease = forms.ChoiceField(choices = DISEASES, required = True,
                              widget = forms.Select(attrs = attrs))
    class Meta:

        model = Diseases
        fields = ['disease']
