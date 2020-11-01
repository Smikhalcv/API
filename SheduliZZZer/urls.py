from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import GetData

app_name = 'SheduliZZZer'

urlpatterns = [
    path('get_data/', GetData.as_view()),
]

urlpatterns += staticfiles_urlpatterns()