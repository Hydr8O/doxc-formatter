from django.shortcuts import render, redirect
from pathlib import Path
from django.conf import settings
from docx import Document
from django.http import FileResponse
from django.contrib import messages

def home(request):
    return render(
        request, 
        'core/home.html'
    )

def about(request):
    return render(
        request,
        'core/about.html'
    )


