from django import forms

class SubmissionForm(forms.Form):
    original_text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter your text here'}))