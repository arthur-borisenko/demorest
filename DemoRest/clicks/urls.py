from django.urls import path, include
from clicks.views import *

app_name="clicker"
urlpatterns = [
    path("clicks/create",ClickCreateView.as_view())
]