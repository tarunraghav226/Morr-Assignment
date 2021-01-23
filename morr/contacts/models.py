from django.db import models

# Create your models here.
class ContactsModel(models.Model):
    _id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email_id = models.CharField(unique=True, max_length=30)

    def __str__(self):
        return self._id + " " + self.name + " " + self.email_id
