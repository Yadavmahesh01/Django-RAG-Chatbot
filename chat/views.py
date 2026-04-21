
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ChatMessage

from ai_engine.services.rag_pipline import FinancialRAGEngine

@login_required
def chat_window(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        if question:
            
            # 👉 Instantiate Class and Call Method
            engine = FinancialRAGEngine()
            answer = engine.ask_question(question)
            
            ChatMessage.objects.create(
                user=request.user,
                question=question,
                answer=answer
            )
            
    chat_history = ChatMessage.objects.filter(user=request.user)
    return render(request, 'chat/chat.html', {'chat_history': chat_history})