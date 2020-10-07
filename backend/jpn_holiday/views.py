from rest_framework import generics
from .models import JpnHoliday
from .serializers import JpnHolidaySerializer


class JpnHolidayList(generics.ListAPIView):
    serializer_class = JpnHolidaySerializer

    def get_queryset(self):
        queryset = JpnHoliday.objects.all()
        date = self.request.query_params.get('date')
        name = self.request.query_params.get('name')

        if date:
            queryset = queryset.filter(date__contains=date)
        elif name:
            queryset = queryset.filter(name__contains=name)

        return queryset
