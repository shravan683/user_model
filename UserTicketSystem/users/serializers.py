from rest_framework import serializers
from .models import Ticket
# from django.contrib.auth import get_user_model

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'  
    # class Meta:
    #     model = get_user_model()
    #     fields = '__all__'