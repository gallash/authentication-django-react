"""registration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from setup import views


router = routers.DefaultRouter()
router.register('users', views.UserViewSet, 'user')
router.register('groups', views.GroupViewSet)

# router.register('connection_test', views.ConnectionTest)  
# Doing the above would require additional configuration for
# ConnectionTest, including (but not limited to) "get_extra_actions". It is
# best to not add it to the DefaultRouter (since I am extending from APIView)
# and add it manually into "urlpatterns".


urlpatterns = [
    path('', include(router.urls)),
    path('connection-test-function-based', include('setup.urls')),
    path('connection-test', views.ConnectionTest.as_view(), name="connection-test"),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))  # Does this line automatically creates for me the connection to the API endpoints?
]
