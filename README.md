# ElectroHelp AI – Generative AI Customer Support Assistant

## Project Overview

ElectroHelp AI is a Generative AI-powered customer support chatbot designed to help customers with technology-related questions, product information, and basic troubleshooting.

The application uses a Large Language Model (LLM) combined with Retrieval-Augmented Generation (RAG) to retrieve relevant information from a product knowledge base and generate helpful responses.

## Features

- AI-powered customer support chatbot
- Natural language conversations
- Conversation history and memory
- Retrieval-Augmented Generation (RAG)
- Product information retrieval
- ChromaDB vector database
- Semantic search using text embeddings
- FastAPI backend
- Web-based chatbot interface

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend development |
| FastAPI | API development |
| Groq API | LLM inference |
| OpenAI-compatible Python client | Communication with the LLM API |
| Sentence Transformers | Text embeddings |
| ChromaDB | Vector database |
| HTML | Frontend structure |
| CSS | Frontend styling |
| JavaScript | Chat functionality |

## System Architecture

1. The user submits a question through the chatbot interface.
2. The frontend sends the question to the FastAPI backend.
3. The RAG system searches the product knowledge base for relevant information.
4. Retrieved information is provided to the language model as context.
5. The language model generates a response.
6. The response is returned to the frontend and displayed to the user.

## Project Structure

```text
electrohelp-ai/
│
├── main.py
├── requirements.txt
├── README.md
│
├── static/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── knowledge_base/
│   ├── chunk_processor.py
│   ├── document_processor.py
│   ├── embedding_generator.py
│   ├── product_loader.py
│   ├── product_search.py
│   └── vector_store.py
│
├── chroma_db/
│
└── docs/
    └── RAG-Testing-Results.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd electrohelp-ai
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows Git Bash:

```bash
source venv/Scripts/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the project root and add your Groq API key:

```text
GROQ_API_KEY=your_groq_api_key
```

Never commit your actual API key to GitHub.

### 6. Start the application

```bash
uvicorn main:app --reload
```

### 7. Open the application

Visit:

http://127.0.0.1:8000/

## Testing and Quality Assurance

The chatbot was tested using functional RAG test cases covering:

- Product information retrieval
- Product recommendation relevance
- General technical questions
- Technical troubleshooting
- Response accuracy and relevance
- Conversation memory
- Unsupported product information

Testing documentation is available in:

`docs/RAG-Testing-Results.md`

The project also includes response improvements designed to reduce irrelevant product recommendations and unsupported product claims.

## Future Improvements

- Expand the product knowledge base.
- Improve product retrieval relevance.
- Add more comprehensive automated tests.
- Improve chatbot response formatting.
- Deploy the application online.

## Project Purpose

This project demonstrates practical Generative AI engineering concepts, including LLM integration, prompt engineering, embeddings, vector databases, semantic search, Retrieval-Augmented Generation, API development, and chatbot development.