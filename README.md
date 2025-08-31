# 📚 Apple QA RAG

## 📋 Deskripsi
Projek ini adalah projek latihan saya untuk membuat aplikasi untuk Proyek ini adalah Question Answering System berbasis Retrieval-Augmented Generation (RAG) untuk menjawab pertanyaan seputar iPhone. Sistem ini memanfaatkan Large Language Model (LLM) dan vector database untuk mengambil informasi relevan dari dokumen sebelum menghasilkan jawaban.

## 🚀 Fitur
- Dataset disimpan dalam bentuk CSV
- Menjawab pertanyaan seputar produk Apple
- Antarmuka sederhana menggunakan Streamlit
- Menggunakan RAG untuk menggabungkan retrieval + model LLM

## 🧠 Tools & Library
- Python
- Langchain
- Streamlit
- Chromadb
- Pandas
- LLM

## 📁 Struktur Folder
- Apple QA RAG/
  - data
      - apple.csv
  - src
      - chroma_db
      - chatbot.ipynb
  - streamlit.py
  - requirements.txt
  - README.md
 
🛠️ Arsitektur
1. Load Dataset
2. Cleaning Data
3. Convert csv menjadi dokumen
4. Chunking : memecah teks yang besar menjadi beberapa bagian kecil
5. Embedding : mengubah teks menjadi vektor angka
6. Vector Store : Menyimpan vektor angka ke vector database
7. Retriever : mencari dari vector database hasil yang paling mirip untuk diambil
8. LLM : Memproses jawaban dari konteks kemiripan dari retriever

## 🖥️ Cara Menjalankan Program
