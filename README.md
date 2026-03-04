# 📄 Smart Document Q&A Bot

An AI-powered chatbot that allows users to **upload PDF documents and ask questions about the content**.
The system reads the document, extracts the text, and uses a Large Language Model to generate answers based on the document context.

This project demonstrates a **basic document question-answering system using LLM context injection**.

---

# 🚀 Features

* Upload PDF documents
* Ask questions related to the document
* AI-generated answers using document context
* Document summarization (e.g., *"Explain the document"*)
* Logging for debugging and monitoring
* Simple and interactive UI using Streamlit

---

# 🧠 How It Works

The system follows a simple pipeline:

1. User uploads a **PDF document**
2. The application **extracts text from the PDF**
3. The user asks a **question about the document**
4. The document text and question are sent to the LLM
5. The LLM generates an answer based on the document context
6. The answer is displayed in the Streamlit interface

---

# 🏗 Architecture

```
User
  │
  ▼
Streamlit UI (app.py)
  │
  ▼
PDF Reader (pdf_reader.py)
  │
Extract Text from Document
  │
  ▼
Prompt Builder
(Document Context + User Question)
  │
  ▼
LLM API (Gemini 2.5 Flash)
  │
  ▼
Generated Answer
  │
  ▼
Displayed in Streamlit UI
```

---

# 🛠 Tech Stack

* **Python**
* **Streamlit** – UI framework
* **Google Gemini API** – Large Language Model
* **PyPDF** – PDF text extraction
* **python-dotenv** – Environment variable management
* **Logging** – Debugging and monitoring

---

# 📂 Project Structure

```
smart-document-qa-bot
│
├── app.py              # Streamlit application
├── pdf_reader.py       # PDF text extraction
├── llm.py              # LLM integration
├── logger.py           # Logging configuration
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
├── .gitignore          # Ignored files for Git
└── .env                # API keys (not pushed to GitHub)
```

---

# ⚙️ Installation

Clone the repository:

```
git clone https://github.com/your-username/smart-document-qa-bot.git
cd smart-document-qa-bot
```

---

# 🧪 Create Virtual Environment

```
python -m venv Smart_Document_QA_Bot
```

Activate the environment:

**Windows**

```
Smart_Document_QA_Bot\Scripts\activate 
```

**Mac/Linux**

```
source venv/bin/activate
```

---

# 📦 Install Dependencies

```
pip install -r requirements.txt
```

---

# 🔑 Setup API Key

Create a `.env` file in the project root:

```
GOOGLE_API_KEY=your_api_key_here
```

You can obtain an API key from **Google AI Studio**.

---

# ▶️ Run the Application

```
streamlit run app.py
```

Then open the browser at:

```
http://localhost:8501
```

---

# 💡 Example Usage

Upload a document such as:

* Company policy
* Research paper
* Resume
* Technical documentation

Example questions:

```
What is the leave policy?
Who is the author of the document?
Explain the document
Summarize the key points
```

---

# ⚠️ Limitations

This project sends the **entire document to the LLM**, which may cause:

* Token limits for large documents
* Slower response times
* Higher API usage for large files

---

# 🔮 Future Improvements

* Implement **RAG (Retrieval Augmented Generation)**
* Add **document chunking**
* Use **embeddings and vector databases (FAISS)**
* Support multiple document uploads
* Add chat history / conversation memory

---

# 🎯 Learning Outcomes

This project demonstrates:

* LLM API integration
* Prompt engineering
* Document processing
* Building AI applications with Streamlit
* Logging and debugging in AI systems

---

# 👨‍💻 Author

Developed as part of learning projects in **Generative AI and LLM applications**.

---

# ⭐ If you find this project useful

Give the repository a **star ⭐ on GitHub**.
