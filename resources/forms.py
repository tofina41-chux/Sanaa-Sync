from django import forms
from .models import Booking, GigApplication

class BookingForm(forms.ModelForm):
    """
    Form for the general booking details (The 'Who', 'When', and 'What event').
    """
    start_time = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control', 'required': 'required'})
    )
    end_time = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control', 'required': 'required'})
    )
    event_title = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'e.g. Band Rehearsal, Podcast Session, or Workshop',
            'class': 'form-control',
            'style': 'background: #000; border: 2px solid #222; color: #fff; padding: 10px; border-radius: 8px;'
        }),
        help_text="Give your booking a name so staff know what it's for."
    )

    class Meta:
        model = Booking
        fields = ['event_title', 'start_time', 'end_time']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class GigApplicationForm(forms.ModelForm):
    voice_message = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'accept': 'audio/*'}),
        help_text="Upload a voice recording if you prefer not to write."
    )

    class Meta:
        model = GigApplication
        fields = ['message', 'voice_message']
        widgets = {
            'message': forms.Textarea(attrs={
                'placeholder': 'Why are you the right artist for this gig?',
                'style': 'width: 100%; height: 200px; background: #000; border: 2px solid #222; border-radius: 8px; color: #fff; padding: 20px; font-family: inherit; font-size: 1rem; outline: none; transition: 0.3s; resize: vertical;',
                'onfocus': "this.style.borderColor='#007bff'",
                'onblur': "this.style.borderColor='#222'"
            })
        }

    def clean(self):
        cleaned_data = super().clean()
        message = cleaned_data.get('message')
        voice_message = cleaned_data.get('voice_message')
        
        if not message and not voice_message:
            raise forms.ValidationError("Please provide either a text message or a voice recording.")
        
        return cleaned_data