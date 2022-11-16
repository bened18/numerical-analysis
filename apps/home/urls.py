from django.urls import path

from apps.home.views import HomeTemplateView

app_name = "home"

urlpatterns = [
    path(
        '',
        HomeTemplateView.as_view(),
        name='index',
    ),
]
