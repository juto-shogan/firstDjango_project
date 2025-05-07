from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
        # fields = ['first_name', 'last_name', 'guest_count', 'resevatation_date', 'comments']
        