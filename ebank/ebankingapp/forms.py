# forms.py
from django import forms
from.models import District,Branch,Account

class YourForm(forms.Form):
    name = forms.CharField(label='Name')
    dob = forms.DateField(label='Date of Birth', widget=forms.DateInput(attrs={'type': 'date'}))
    age = forms.IntegerField(label='Age')
    GENDER_CHOICES = [('male', 'Male'), ('female', 'Female')]
    gender = forms.ChoiceField(label='Gender', choices=GENDER_CHOICES, widget=forms.RadioSelect)
    phone_number = forms.CharField(label='Phone Number', max_length=15)
    email = forms.EmailField(label='Email')
    address = forms.CharField(label='Address', widget=forms.Textarea)
    district = forms.ModelChoiceField(queryset=District.objects.all(), label='District', empty_label="Select District")

    branch = forms.ModelChoiceField(queryset=Branch.objects.all(), label='Branch', empty_label="Select Branch")
    accounttype = forms.ModelChoiceField(queryset=Account.objects.all(), label='AccountType',
                                         empty_label='Select AccountType')
    MATERIAL_CHOICES = [('cheque', 'cheque'), ('debitcard', 'debitcard'), ('creditcard', 'creditcard')]
    materials_provided = forms.MultipleChoiceField(label='Materials Provided', choices=MATERIAL_CHOICES, widget=forms.CheckboxSelectMultiple)

