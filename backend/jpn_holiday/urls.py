from django.urls import path
from . import views


app_name = 'jpn_holiday'
urlpatterns = [
    path('jpn_holiday/', views.JpnHolidayList.as_view(), name='jpn_holiday'),
]
