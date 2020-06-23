"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from testapp.views import Test, CreateGenre, UpdateGenre, ListGenre, DeleteGenre

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/<int:pk>', Test.as_view()),
    path('create-genre/', CreateGenre.as_view()),
    path('update-genre/<int:pk>', UpdateGenre.as_view()),
    path('list-genre/', ListGenre.as_view()),
    path('delete-genre/<int:pk>', DeleteGenre.as_view()),

    # http://127.0.0.1:8000/test/6
   
]
