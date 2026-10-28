
# RAG Chatbot

A document-based AI chatbot that lets users upload PDF documents and ask questions about their content. It uses Retrieval-Augmented Generation (RAG) to retrieve relevant text and generate answers grounded in the uploaded documents.

## Features

- **PDF upload:** Upload a document and process its content for question answering.
- **RAG pipeline:** Retrieve relevant document chunks before generating a response.
- **AI-powered answers:** Uses OpenRouter-compatible chat and embedding models.
- **Source references:** Displays source information, including page numbers, to help users verify answers.
- **Web interface:** React-based frontend for document uploads and interactive chat.
- **API backend:** FastAPI handles document ingestion and chat requests.
- **Local vector storage:** Uses an in-memory vector store with JSON persistence for stored embeddings and document chunks.

## Tech Stack

| Component | Technology |
|---|---|
| Frontend | React, Vite, JavaScript, CSS |
| Backend | Python, FastAPI |
| AI integration | OpenRouter API |
| Embeddings | NVIDIA Nemotron embedding model via OpenRouter |
| Retrieval | LangChain InMemoryVectorStore |
| Storage | Local JSON persistence |
| Version control | Git and GitHub |

## How It Works

1. Upload a PDF through the web interface.
2. The backend extracts and splits the document text into chunks.
3. The embedding model converts the chunks into vectors.
4. Relevant chunks are retrieved when a user asks a question.
5. The chat model generates an answer using the retrieved context.
6. The application returns the answer with source references where available.

## Project Structure

```text
RAG-CHATBOT/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── db/
│   │   └── services/
│   ├── tests/
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   └── assets/
│   ├── package.json
│   └── vite.config.js
├── render.yaml
├── .gitignore
└── README.md
```

## Prerequisites

- Python 3.12 recommended
- Node.js and npm
- An OpenRouter API key with access to the configured models

## Setup and Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/SagarDAS200/RAG-CHATBOT.git
cd RAG-CHATBOT
```

### 2. Configure the backend

Open a terminal in the project root:

```bash
cd backend
py -3.12 -m venv venv
```

Activate the virtual environment on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Install the Python dependencies:

```bash
python -m pip install -r requirements.txt
```

Create a `.env` file inside `backend/` and configure the environment variables required by `backend/app/core/config.py`. Add your OpenRouter API key locally; never commit your `.env` file or publish your API key.

Start the backend from the `backend/` directory:

```bash
python -m uvicorn app.main:app --reload
```

Backend URL: `http://127.0.0.1:8000`

### 3. Configure the frontend

Open a second terminal from the project root:

```bash
cd frontend
npm install
npm run dev
```

Open the local URL printed by Vite, typically `http://localhost:5173`.

## Usage

1. Start both the backend and frontend.
2. Open the frontend in your browser.
3. Upload a PDF document.
4. Wait for document processing to finish.
5. Ask questions about the uploaded document.
6. Review the generated answer and its source references.

## Security Notes

- Keep API keys in local environment variables.
- Never commit `.env` files, private documents, or local vector-store data.
- Do not upload confidential documents to services unless you are authorized to do so.
- API and model availability may depend on your OpenRouter account and the models currently accessible to it.

## Future Improvements

- Add automated tests for document ingestion and retrieval.
- Improve retrieval quality and source attribution.
- Add support for more document formats.
- Add deployment instructions and a hosted demo.
- Improve error handling and loading feedback.

## Author

**Sagar Das**

- GitHub: [SagarDAS200](https://github.com/SagarDAS200)
- LinkedIn: [sagardas200](https://www.linkedin.com/in/sagardas200/)

---

*An educational project demonstrating document ingestion, semantic retrieval, and AI-powered question answering using Retrieval-Augmented Generation.*
