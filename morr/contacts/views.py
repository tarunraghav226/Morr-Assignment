from django.shortcuts import render
from rest_framework import generics
from .models import ContactsModel
from .serializers import ContactSerializer

# Create your views here.
class ContactListAPIView(generics.ListAPIView):
    queryset = ContactsModel.objects.all()
    serializer_class = ContactSerializer


class ContactDetailAPIView(generics.RetrieveAPIView):
    queryset = ContactsModel.objects.all()
    serializer_class = ContactSerializer
    lookup_field = "_id"


class AddContactAPIView(generics.CreateAPIView):
    serializer_class = ContactSerializer
