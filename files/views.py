from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, FileResponse
from django.contrib import messages
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from .models import UserFile
from .forms import UserFileForm
import os
import mimetypes

@login_required
def file_list(request):
    files = UserFile.objects.filter(user=request.user)
    return render(request, 'files/file_list.html', {'files': files})

@login_required
def file_upload(request):
    if request.method == 'POST':
        form = UserFileForm(request.POST, request.FILES)
        if form.is_valid():
            user_file = form.save(commit=False)
            user_file.user = request.user
            user_file.save()
            messages.success(request, 'File uploaded successfully!')
            return redirect('files:file_list')
    else:
        form = UserFileForm()
    
    context = {
        'form': form,
        'max_size': settings.MAX_UPLOAD_SIZE / 1024 / 1024,  # Convert to MB
        'allowed_types': settings.ALLOWED_FILE_TYPES
    }
    return render(request, 'files/file_upload.html', context)

@login_required
def file_download(request, pk):
    user_file = get_object_or_404(UserFile, pk=pk, user=request.user)
    file_path = user_file.file.path
    
    if os.path.exists(file_path):
        content_type, _ = mimetypes.guess_type(file_path)
        if content_type is None:
            content_type = 'application/octet-stream'
            
        response = FileResponse(
            open(file_path, 'rb'),
            content_type=content_type
        )
        response['Content-Disposition'] = f'attachment; filename="{user_file.filename}"'
        return response
    
    messages.error(request, 'File not found!')
    return redirect('files:file_list')

@login_required
def file_delete(request, pk):
    user_file = get_object_or_404(UserFile, pk=pk, user=request.user)
    
    if request.method == 'POST':
        user_file.delete()
        messages.success(request, 'File deleted successfully!')
        return redirect('files:file_list')
    
    return render(request, 'files/file_delete.html', {'file': user_file})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! Please login.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
