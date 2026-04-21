# Django-RAG-Chatbot
A production-ready, multi-user Document RAG Chatbot built with Django, FAISS, and Groq (LLaMA 3.1). Upload any PDF and chat with it instantly.
Enterprise Django RAG: Multi-User Document AI Platform
Most AI projects on GitHub are fragile, single-user Python scripts that collapse in production. This project bridges the critical gap between an AI prototype and scalable enterprise software. It is a production-grade, full-stack Retrieval-Augmented Generation (RAG) platform built natively on Django. It empowers multiple authenticated users to securely upload, vectorize, and chat with any type of document—ranging from complex financial reports to massive technical manuals—in an isolated, private environment.
Engineered with strict adherence to Software Engineering first principles, this repository demonstrates how to properly architect scalable AI web applications. It abandons messy script code in favor of a deeply modular, class-based Object-Oriented architecture. By enforcing a rigorous separation of concerns across AI services, database ORMs, and UI routing, the system is exceptionally maintainable. If business requirements change—such as swapping local FAISS for cloud-based Pinecone, or migrating from Groq to OpenAI—developers only need to modify a single utility module without breaking the core application.
Core System Capabilities:
Enterprise Authentication: Secure, session-backed user isolation ensuring users only access their own proprietary documents and data.
Automated Ingestion Pipeline: Seamless PDF uploads trigger immediate text extraction, recursive character chunking, and local vectorization.
High-Fidelity Retrieval: Utilizes FAISS and HuggingFace local embeddings to mathematically isolate and retrieve only the most relevant document context.
Blazing Fast Generation: Deep integration with Groq’s API (LLaMA-3.1) guarantees instantaneous, contextually grounded AI responses.
Persistent Conversation State: Relational database mapping links users to their entire chat histories for seamless workflow continuity.
Technical Stack:
Backend & UI: Django, SQLite
AI Engine: LangChain, PyPDF2
Vector Database: FAISS, Sentence-Transformers (all-MiniLM)
LLM Provider: Groq (LLaMA-3.1-8b)
This repository represents the modern standard for full-stack AI engineering, proving that deploying intelligent LLMs requires robust backend architecture, not just simple API calls.

**new branch** 
#this is for the pr understandingS