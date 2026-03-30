# AI-Log-Analysis-and-RCA-bot
An AI-powered log analysis application that automatically analyzes system log files and performs Root Cause Analysis (RCA) using Retrieval-Augmented Generation (RAG).

The application loads log files, converts them into embeddings, stores them in a vector database, and allows users to ask questions about system failures using a Large Language Model.

The user interface is built using Streamlit for interactive analysis.

🚀 Features
📄 Load and process system log files
🔎 Semantic search on logs
🤖 AI-powered Root Cause Analysis
⚡ Fast inference using Groq
🧠 Retrieval-Augmented Generation using LangChain
📊 Vector storage using Chroma
🌐 Interactive web interface

🧠 Technologies Used
| Component       | Technology            |
| --------------- | --------------------- |
| Language        | Python                |
| LLM             | Llama 3.1             |
| Framework       | LangChain             |
| Vector Database | Chroma                |
| Embeddings      | Sentence Transformers |
| UI              | Streamlit             |
| API Provider    | Groq                  |

📂 Project Structure

GenAI_log_RCA
│
├── main.py                 # Streamlit user interface
├── data_process.py         # Log processing & RAG pipeline
│
├── docs
│   └── debug.log           # Sample log file
│
├── resources
│   └── vectorstore         # Chroma vector database
│
├── .env                    # API keys
├── requirements.txt
└── README.md

⚙️ Installation
1️⃣ Clone the repository
git clone https://github.com/yourusername/log-analysis-rca.git
cd log-analysis-rca

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Configure environment variables
Create a .env file in the project root.
GROQ_API_KEY=your_api_key_here

▶️ Running the Application
streamlit run main.py

⚙️ How It Works
1️⃣ Log Loading

Log files are loaded using a text loader.

2️⃣ Text Splitting

Logs are divided into smaller chunks for efficient embedding.

3️⃣ Embedding Generation

Embeddings are generated using the model:

sentence-transformers/all-MiniLM-L6-v2
4️⃣ Vector Storage

Embeddings are stored in a Chroma vector database.

5️⃣ Retrieval + LLM Analysis

Relevant log segments are retrieved and passed to the LLM for analysis.

👨‍💻 Author

Senthil Prabhu A

AI | Machine Learning | Generative AI
