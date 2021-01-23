from django.shortcuts import render
from rest_framework import generics
from .models import ContactsModel
from .serializers import ContactSerializer

# Create your views here.
class ContactListAPIView(generics.ListAPIView):
    """
        This view returns the list of contacts available.
    """
    queryset = ContactsModel.objects.all()
    serializer_class = ContactSerializer
    pagination_class = None


class ContactDetailAPIView(generics.RetrieveAPIView):
    """
        This view returns the detail of specific contact.
    """
    queryset = ContactsModel.objects.all()
    serializer_class = ContactSerializer
    lookup_field = "_id"


class AddContactAPIView(generics.CreateAPIView):
    """
        This view adds a new contact in database.
    """
    serializer_class = ContactSerializer


class DeleteContactAPIView(generics.DestroyAPIView):
    """
        This view deletes the contact from database.
    """
    queryset = ContactsModel.objects.all()
    serializer_class = ContactSerializer
    lookup_field = "_id"


class UpdateContactAPIView(generics.UpdateAPIView):
    """
        This view updates the contact if available.
    """
    queryset = ContactsModel.objects.all()
    serializer_class = ContactSerializer
    lookup_field = "_id"


class SearchContactAPIVIew(generics.ListAPIView):
    """
        This view returns the list of contacts available after searching them in database and 
        also uses pagination.
    """
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