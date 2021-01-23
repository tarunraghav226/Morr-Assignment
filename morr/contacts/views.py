from django.shortcuts import render
from rest_framework import generics
from .models import ContactsModel
from .serializers import ContactSerializer

# Create your views here.
class ContactListAPIView(generics.ListAPIView):
    queryset = ContactsModel.objects.all()
    serializer_class = ContactSerializer
