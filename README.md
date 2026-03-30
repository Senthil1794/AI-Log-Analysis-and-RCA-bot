# AI-Log-Analysis-and-RCA-bot
AI log analysis bot that process log file and find the reason of error and respond to user
🔍 AI Log Analysis & Root Cause Analysis Bot

An AI-powered Log Analysis application that analyzes system logs and performs Root Cause Analysis (RCA) using Retrieval-Augmented Generation (RAG).

The system reads log files, converts them into embeddings, stores them in a vector database, and uses an LLM to answer troubleshooting queries.

The application interface is built using Streamlit.

✅ Automated log file ingestion
✅ Semantic search on logs
✅ Root Cause Analysis using LLM
✅ Vector database storage
✅ Interactive UI using Streamlit
✅ Fast inference using Groq LLM

🧠 System Architecture

Log File (debug.log)
        │
        ▼
Text Loader
        │
        ▼
Text Splitter
        │
        ▼
Embeddings Model
        │
        ▼
Vector Database (Chroma)
        │
        ▼
Retriever
        │
        ▼
Groq LLM
        │
        ▼


Root Cause Analysis
| Component    | Technology            |
| ------------ | --------------------- |
| LLM          | Llama 3.1             |
| Framework    | LangChain             |
| Vector DB    | Chroma                |
| Embeddings   | Sentence Transformers |
| UI           | Streamlit             |
| API Provider | Groq                  |
| Language     | Python                |
       


📂 Project Structure

log-rca-bot
│
├── main.py              # Streamlit UI
├── data_process.py      # Log processing and RAG pipeline
│
├── docs
│   └── debug.log        # Input log file
│
├── resources
│   └── vectorstore      # Chroma vector DB storage
│
├── .env                 # API keys
├── requirements.txt
└── README.md


⚙️ Installation
1️⃣ Clone Repository
git clone https://github.com/yourusername/log-rca-bot.git
cd log-rca-bot
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Setup Environment Variables

Create a .env file in the project root.

GROQ_API_KEY=your_api_key_here
▶️ Run the Application

Start the Streamlit app:

streamlit run main.py

The UI will open in your browser.

🖥 Application Interface
Step 1 — Process Logs

Click Process logs to:

• Load log file
• Split logs into chunks
• Generate embeddings
• Store embeddings in vector database

Step 2 — Ask RCA Questions

Enter questions such as:

What is the root cause of the error?

Find the critical failures in logs.

Why did the system crash?

Which module is failing?

Then click RCA.

The system retrieves relevant log segments and generates a response using the LLM.

⚙️ How It Works
1️⃣ Log Loading

Logs are loaded using:

TextLoader
2️⃣ Text Splitting

Logs are split into smaller chunks using:

RecursiveCharacterTextSplitter
3️⃣ Embeddings Generation

Embeddings are generated using:

sentence-transformers/all-MiniLM-L6-v2
4️⃣ Vector Storage

Embeddings are stored in:

Chroma Vector Database
5️⃣ Retrieval + LLM Reasoning

The pipeline uses:

RetrievalQAWithSourcesChain

Steps:

1️⃣ Retrieve relevant log chunks
2️⃣ Send them to the LLM
3️⃣ Generate Root Cause Analysis

📊 Example Output

Example RCA response:

Root Cause Analysis:

The system failure occurred due to repeated
database connection timeouts.

Multiple ERROR logs indicate that the database
service was unreachable between 12:45 and 12:50,
causing the application to crash.
💡 Use Cases

This project can be used for:

• DevOps log troubleshooting
• AI-powered observability
• Incident root cause analysis
• Security log investigation
• Production system monitoring

🔮 Future Improvements

Possible enhancements:

• Real-time log monitoring
• Multiple log file ingestion
• Kubernetes log integration
• Anomaly detection
• Automated alert generation

👨‍💻 Author

Senthil Prabhu A

AI | Machine Learning | Generative AI Enthusiast
