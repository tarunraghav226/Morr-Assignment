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


class DeleteContactAPIView(generics.DestroyAPIView):
    queryset = ContactsModel.objects.all()
    serializer_class = ContactSerializer
    lookup_field = "_id"


class UpdateContactAPIView(generics.UpdateAPIView):
    queryset = ContactsModel.objects.all()
    serializer_class = ContactSerializer
    lookup_field = "_id"


class SearchContactAPIVIew(generics.ListAPIView):
    serializer_class = ContactSerializer

    def get_queryset(self):
        if self.request.GET.get("name",None) and self.request.GET.get("email_id",None):
            return ContactsModel.objects.filter(name = self.request.GET["name"], email_id = self.request.GET["email_id"])
        elif self.request.GET.get("name",None):
            return ContactsModel.objects.filter(name = self.request.GET["name"])
        elif self.request.GET.get("email_id",None):
            return ContactsModel.objects.filter(email_id = self.request.GET["email_id"])
        else:
            return ContactsModel.objects.all()