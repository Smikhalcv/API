from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import GetEvents, GetExperts, UpdateEvents, UpdateExperts, UpdateImages, UpdateDefaultEvents

app_name = "main_app"

urlpatterns = [
    path("get_events/", GetEvents.as_view()),
    path("get_experts/", GetExperts.as_view()),
    path("update_events/", UpdateEvents.as_view()),
    path("update_experts/", UpdateExperts.as_view()),
    path("update_images/", UpdateImages.as_view()),
    path("update_default_events/", UpdateDefaultEvents.as_view()),
]

urlpatterns += staticfiles_urlpatterns()
