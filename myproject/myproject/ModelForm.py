from django.forms import ModelForm
from myapp.models import Reservation

class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'seats', 'content', 'reporter']