from django.db import models

class Article(models.Model):
    content=models.CharField(max_length=200)
    user_name=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.content
# -------------------------------
class Document(models.Model):
    description=models.CharField(max_length=255,blank=True)
    photo=models.ImageField(upload_to="documents/",default="defo")
    upload_at=models.DateTimeField(auto_now_add=True)
