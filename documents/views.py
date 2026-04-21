
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import DocumentUploadForm
from .models import Document
from django.contrib import messages


from ai_engine.services.rag_pipline import FinancialRAGEngine 

@login_required
def document_list(request):
    documents = Document.objects.filter(user=request.user)
    
    if request.method == 'POST':
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save(commit=False)
            doc.user = request.user
            doc.save() 
            
            try:
                
                engine = FinancialRAGEngine()
                engine.ingest_document(doc.file.path)
                
                doc.is_indexed = True
                doc.save()
                messages.success(request, f"Successfully uploaded and indexed {doc.file.name}!")
            except Exception as e:
                doc.delete() 
                messages.error(request, f"AI Processing failed: {str(e)}")
                
            return redirect('document_list')
    else:
        form = DocumentUploadForm()

    return render(request, 'documents/upload.html', {'form': form, 'documents': documents})