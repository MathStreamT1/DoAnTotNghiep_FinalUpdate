from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render,get_object_or_404
from .models import Document

def document_list(request):
    documents = Document.objects.all()

    # Number of documents to display per page
    items_per_page = 10

    # Create a Paginator instance
    paginator = Paginator(documents, items_per_page)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')

    try:
        # Get the documents for the requested page
        documents = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        documents = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        documents = paginator.page(paginator.num_pages)

    return render(request, 'document/document_list.html', {'documents': documents})


def document_detail(request, pk):
    document = get_object_or_404(Document, pk=pk)
    return render(request, 'document/document_detail.html', {'document': document})
