from django.urls import path
from . import views


urlpatterns = [
    path('', views.connection_test, name="connection-test-function-based")
]
