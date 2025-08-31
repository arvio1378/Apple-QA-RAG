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
- LLM ()

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
5. Embedding : mengubah teks menjadi vektor angka (Qwen/Qwen3-Embedding-0.6B)
6. Vector Store : Menyimpan vektor angka ke vector database
7. Retriever : mencari dari vector database hasil yang paling mirip untuk diambil
8. LLM : Memproses jawaban dari konteks kemiripan dari retriever (llama3)

## 🖥️ Cara Menjalankan Program
1. Clone repositori
```bash
git clone https://github.com/arvio1378/Apple-QA-RAG.git
cd Apple QA RA
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Jalankan Program
```bash
streamlit run streamlit.py
```

## 📊 Dataset
| Question    | Answer      |
|-------------|-------------|
| How do I take a screenshot on an iPhone? | To take a screenshot on an iPhone, press and hold the Side button and the Volume Up button simultaneously. The screen will flash briefly, and a thumbnail of the screenshot will appear in the bottom-left corner of the screen. Tap the thumbnail to view or edit the screenshot. |
| How do I change my wallpaper on an iPhone?         | To change your wallpaper on an iPhone, go to Settings > Wallpaper. Select whether you want to change the wallpaper for your Lock Screen, Home Screen, or both. Choose from a variety of built-in wallpapers or use your own photos.         |
| How do I make a phone call on an iPhone?       | To make a phone call on an iPhone, open the Phone app and tap the Contacts tab. Find the contact you want to call and tap their name. Alternatively, you can enter a phone number manually in the dial pad.         |
| How do I send a text message on an iPhone?        | To send a text message on an iPhone, open the Messages app and tap the New Message button. Enter the name or phone number of the person you want to text, and then type your message. Tap the Send button when you're done.          |
| ...         | ...         |

Information about dataset attributes :
- Question : Pertanyaan seputar produk apple
- Answer : Jawaban dari pertanyaan produk apple yang ditanyakan

## 📈 Hasil & Evaluasi
Berikut ini adalah beberapa pertanyaan dan bagaimana model dapat menjawab pertanyaan tersebut.
1. - Question : Can i use calculator on iphone and how ?
   - System : According to the previous questions and answers, you can use the Calculator app on an iPhone by:
       - Opening the Calculator app.
       - Using the standard calculator interface to perform basic arithmetic operations (addition, subtraction, multiplication, and division).
       - Swiping to the left to reveal a scientific calculator with more advanced functions.
     So, to answer your question: To use the calculator on your iPhone, open the Calculator app and start performing calculations using the basic or scientific calculator interfaces!

2. - Question : How to check RAM of a mac ?
   - System : According to the provided context, to check the amount of RAM in your Mac:
     Helpful Answer: Click on the Apple menu and select "About This Mac", it will display the amount of RAM.

3. - Question : Can I use keyboard and mouse for apple TV ?
   - System : According to the provided context, it seems that:
     Yes, you can pair a Bluetooth keyboard and mouse with your Apple TV.

Dari Hasil tersebut dapat disimpulkan bahwa model dapat menjawab pertanyaan sesuai konteks yang ditanyakan dengan baik dan sesuai.

## 🏗️ Kontribusi
Dapat melakukan kontribusi kepada siapa saja. Bisa bantu untuk :
- Menggunakan dataset yang lebih banyak dan kompleks
- Mencoba dengan model LLM yang berbeda
- Menyempurnakan desain dari streamlit menjadi lebih bagus

## 🧑‍💻 Tentang Saya
Saya sedang belajar dan membangun karir di bidang AI/ML. Projek ini adalah latihan saya untuk membangun aplikasi python sederhana. Saya ingin lebih untuk mengembangkan skill saya di bidang ini melalui projek-projek yang ada.

📫 Terhubung dengan saya di:
- Linkedin : https://www.linkedin.com/in/arvio-abe-suhendar/
- Github : https://github.com/arvio1378
