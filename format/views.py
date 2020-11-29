from pathlib import Path
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import FileResponse
from django.http import Http404
from django.contrib import messages
from format.services.prepare_doc import prepare_to_format
from format.exceptions import TooLargeFileException, WrongFileExtensionException


def format_docx(request):
    if request.method == 'GET':
        return Http404
    else:
        doc = request.FILES.get('doc')
        hyphen = request.POST.get('hyphen')
        try:
            validate_document(doc)
            create_documents_dir_if_not_exists()
            formatted_doc = format_document(doc, hyphen)
            formatted_doc.save(f'{settings.MEDIA_ROOT}/documents/formatted.docx')
            return FileResponse(open(f'{settings.MEDIA_ROOT}/documents/formatted.docx', 'rb'))
        except TooLargeFileException as e:
            messages.error(request, e.message)
        except WrongFileExtensionException as e:
            messages.error(request, e.message)
        return redirect('core:home')
    

def validate_document(doc):
    if not doc:
        raise WrongFileExtensionException
    if doc.content_type != settings.VALID_EXTENSION:
        raise WrongFileExtensionException
    if doc.size > settings.MAX_DOCUMENT_SIZE:
        raise TooLargeFileException

def create_documents_dir_if_not_exists():
    document_dir = Path(f'{settings.MEDIA_ROOT}/documents')
    document_dir.mkdir(parents=True, exist_ok=True)

def format_document(doc, hyphen):
    if hyphen == 'on':
        hyphen = True
    else:
        hyphen = False
    formatted_doc = prepare_to_format(doc, hyphenation=hyphen)
    formatted_doc.style_document()
    return formatted_doc
