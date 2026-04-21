# documents/models.py
from django.db import models
from django.contrib.auth.models import User

class Document(models.Model):
    # ForeignKey links this file to a specific User. CASCADE means if user is deleted, their files are deleted.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # FileField handles saving the actual file to the MEDIA_ROOT/pdfs folder
    file = models.FileField(upload_to='pdfs/')
    
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    # This metadata will be used by our AI Engine later to track if FAISS indexed it
    is_indexed = models.BooleanField(default=False) 

    def __str__(self):
        return f"{self.file.name} - {self.user.username}"