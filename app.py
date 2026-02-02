import streamlit as st
import re
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.llms import Ollama

# Konfigurasi halaman Streamlit
st.set_page_config(
    page_title="Apple Q&A",
    page_icon="📱",
    layout="wide"
)

# Membersihkan teks
def clean_text(text):
    if isinstance(text, str): # cek tipe data apakah string
        # hilangkan tab/enter jadi spasi
        text = re.sub(r"[\n\t\r\xa0]", " ", text)
        # hilangkan simbol aneh
        text = re.sub(r"[^a-zA-Z0-9\s.,!?;:'\"()\-]", "", text)
        # hilangkan spasi ganda jadi spasi
        text = re.sub(r"\s+", " ", text)
        # hapus spasi depan belakang
        return text.strip()
    return text # kalau bukan string kembalikan

@st.cache_resource # load vector store sekali saja
# vektor store
def load_vector_store():
    # model embedding
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # load vector store
    return Chroma(
        persist_directory = "chroma_db",
        embedding_function=embedding_model
    )

@st.cache_resource # agar hanya load model dan chain sekali
# untuk load vektor store dan llm
def load_chain():
    # model LLM
    llm = Ollama(model="llama3")

    # load vector store
    vector_db = load_vector_store()

    # retriever untuk mencari dari db hasil yang paling mirip untuk diambil
    retriever = vector_db.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 5}
    )

    # sebagai mesin tanya jawab
    return RetrievalQA.from_chain_type(
        llm = llm, # model yang digunakan untuk menjawab pertanyaan
        retriever = retriever # mencari jawaban yang paling mirip dengan db
    )

# Navigasi sidebar
st.sidebar.title("Navigation")
# Pilihan Navigasi
pages = st.sidebar.selectbox("Menu : ", ["Test", "Profile"])

# Page 1 : Test
if pages == "Test":
    st.title("Apple Q&A")
    st.subheader("Infomation about Apple")
    st.markdown("---")

    # load sistem tanya jawab
    qa_chain = load_chain()

    # input question
    question = st.chat_input("Your question about apple")
    if question:
        # Proses jawaban
        with st.spinner("Process your answer..."):
            result = qa_chain({"query": question})
            answer = result["result"]

        # tampilkan question & answer
        st.write(question)
        st.success("Answer was found !!!")
        st.write("#### Answer")
        st.write(answer)


# Page 2 : Profile
elif pages == "Profile":
    # Judul aplikasi dan huruf italic
    st.title("Arvio Abe Suhendar")
    # Subheader
    st.subheader("Career Shifter | From Network to AI | Designing Intelligent Futures | Ready to Make an Impact in AI | Python Developer | Machine Learning Engineer | Data Scientist")
    st.markdown("---")

    # About me
    st.write("### 📝 About Me")
    st.write("👨‍💻 I'm a tech enthusiast with a strong foundation in Informatics Engineering from Universitas Gunadarma, where I developed solid analytical thinking, programming, and problem-solving skills.")
    st.write("🔧 After graduating, I began my professional journey as a Junior Network Engineer, managing enterprise network services like VPNIP, Astinet, and SIP Trunk on Huawei and Cisco platforms—handling configurations, service activations, and troubleshooting.")
    st.write("🤖 Over time, my curiosity led me to explore the world of Artificial Intelligence & Machine Learning. I've been actively upskilling through bootcamps and self-learning—covering data preprocessing, supervised & unsupervised learning, and deep learning using Python.")
    st.write("🎯 I'm now transitioning my career into AI/ML, combining my network infrastructure background with my growing expertise in data and intelligent systems. I'm particularly interested in how AI can improve systems, automate operations, and drive smarter decision-making.")
    st.write("🤝 Open to collaborations, mentorship, and new opportunities in the AI/ML space.")
    st.markdown("---")

    tab1, tab2, tab3 = st.tabs(["Education", "Experience", "Skills"])
    with tab1:
        # Pendidikan
        st.write("### 🎓 Education")
        st.write("""
        - **Bachelor of Informatics Engineering**   
        Universitas Gunadarma, 2019 - 2023, GPA 3.82/4.00
            - Built multiple applications (web & desktop) using Java, Python, and PHP in individual and team projects.
            - Built and optimized database systems
            - Learn techniques for solving mathematical problems using programming, numerical integration, and solving equations.
        - **Bootcamp AI/ML**    
        Dibimbing.id Academy, 2025 - Present
            - Mastered core concepts of Python programming including variables, data types, control structures, and functions.
            - Understanding the fundamentals of Artificial Intelligence and Machine Learning, key concepts, and applications.
            - Techniques to clean, transform, and prepare data for analysis, including handling missing data and feature scaling.
        """)
    with tab2:
        # Pengalaman
        st.write("### 💼 Experience")
        st.write("""
        - **Junior Network Engineer**   
        PT. Infomedia Nusantara, 2023 - Present
            - Astinet & VPNIP Service Management (Huawei Routers) : 
                 Handled service activation, disconnection,isolation, modification, and resumption for enterprise clients.
            - Wifi.id Service Provisioning (Cisco & WPgen) :    
                 Performed end-to-end activation and troubleshooting for public Wi-Fi services.
            - SIP Trunk International Access Control :  
                 Managed blocking and unblocking processes for international SIP trunk services to ensure secure and compliant voice connectivity
        """)
    with tab3:
        # Keterampilan
        st.write("### 🛠️ Skills")
        st.write("""
        - **Programming Languages**: Python
        - **Machine Learning**: Scikit-learn, TensorFlow, Keras
        - **Data Analysis**: Pandas, NumPy, Matplotlib, Seaborn
        - **Database Management**: MySQL, PostgreSQL
        - **Networking**: Huawei Routers, Cisco Routers, WPgen
        - **Tools & Technologies**: Git, Docker, Jupyter Notebook
        - **Soft Skills**: Attention to Detail, Team Collaboration, Adaptability
        """)
    
    st.markdown("---")
    # Kontak
    st.write("### 📞 Contact Information")
    st.write("I'm currently studying and building a career in AI/ML. This project is my practice in building a simple Python application. I want to further develop my skills in this field through existing projects.")
    st.write("Feel free to contact me if you have any questions or suggestions regarding this project.")
    st.write("Email: 4rv10suhendar@gmail.com")
    st.write("LinkedIn: [Arvio Abe Suhendar](https://www.linkedin.com/in/arvio-abe-suhendar/)")
    st.write("Location: Depok, Indonesia")
    st.write("GitHub: [Arvio1378](https://github.com/arvio1378)")