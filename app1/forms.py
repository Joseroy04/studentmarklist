from django import forms


class loginForm(forms.Form):
    studentId = forms.CharField( max_length=6, required=True)
    dob = forms.DateField(help_text="enter the Dob", required=True)
