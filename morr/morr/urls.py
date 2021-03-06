"""morr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from contacts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_get/', views.ContactListAPIView.as_view()),
    path('api_get/<int:_id>', views.ContactDetailAPIView.as_view()),
    path('api_add/', views.AddContactAPIView.as_view()),
    path('api_delete/<int:_id>', views.DeleteContactAPIView.as_view()),
    path('api_update/<int:_id>', views.UpdateContactAPIView.as_view()),
    path('api_search/', views.SearchContactAPIVIew.as_view())
]
