from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.conf import settings
import os
import mimetypes

def validate_file_type(value):
    """Validate the file type against allowed extensions"""
    ext = os.path.splitext(value.name)[1].lower()
    if ext not in settings.ALLOWED_FILE_TYPES:
        raise ValidationError(f'File type {ext} is not supported. Allowed types: {", ".join(settings.ALLOWED_FILE_TYPES)}')

def validate_file_size(value):
    """Validate the file size against maximum allowed size"""
    if value.size > settings.MAX_UPLOAD_SIZE:
        raise ValidationError(f'File size cannot exceed {settings.MAX_UPLOAD_SIZE/1024/1024}MB')

def get_file_type_category(filename):
    """Return the category of a file based on its extension"""
    ext = os.path.splitext(filename)[1].lower()
    
    if ext in ['.jpg', '.png']:
        return 'image'
    elif ext in ['.pdf']:
        return 'pdf'
    elif ext in ['.docx', '.doc']:
        return 'document'
    else:
        return 'other'

class UserFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(
        upload_to='uploads/',
        validators=[validate_file_type, validate_file_size]
    )
    filename = models.CharField(max_length=255)
    upload_date = models.DateTimeField(auto_now_add=True)
    file_size = models.IntegerField()
    content_type = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.filename:
            self.filename = self.file.name
        if not self.file_size:
            self.file_size = self.file.size
        if not self.content_type:
            content_type, _ = mimetypes.guess_type(self.file.name)
            self.content_type = content_type or 'application/octet-stream'
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Delete the file from storage when model instance is deleted
        if self.file:
            if os.path.isfile(self.file.path):
                os.remove(self.file.path)
        super().delete(*args, **kwargs)
        
    def get_file_icon(self):
        """Returns the appropriate Font Awesome icon class based on file type"""
        category = get_file_type_category(self.filename)
        
        icons = {
            'image': 'far fa-file-image text-blue-500',
            'pdf': 'far fa-file-pdf text-red-500',
            'document': 'far fa-file-word text-blue-600',
            'other': 'far fa-file text-gray-500'
        }
        
        return icons.get(category, icons['other'])
    
    def get_extension(self):
        """Returns the file extension"""
        return os.path.splitext(self.filename)[1].lower()

    def __str__(self):
        return f'{self.filename} (uploaded by {self.user.username})'

    class Meta:
        ordering = ['-upload_date']
