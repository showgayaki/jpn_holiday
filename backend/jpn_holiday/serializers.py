from rest_framework import serializers
from .models import JpnHoliday


class JpnHolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = JpnHoliday
        fields = ('date', 'name')
