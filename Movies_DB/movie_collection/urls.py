"""
URL configuration for movie_collection project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include  # Import include
from movies.views import register,create_collection, get_request_count


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('movies/', include('movies.urls')),  # This includes the app's URL patterns under the /movies/ prefix
    path('collections/create/', create_collection, name='create_collection'),
    path('request_count/', get_request_count, name='get_request_count'),
]
