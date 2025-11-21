# AI Web Scraper API

![Status](https://img.shields.io/badge/status-active-success.svg)
![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![Model](https://img.shields.io/badge/Model-Llama_3.2-purple)

## 📖 Overview

AI Web Scraper API is designed to extract structured JSON data from websites.

This project leverages **Llama 3.2** for both generation and embedding tasks, prioritizing low-latency inference and high-efficiency deployment.

## 🧠 Model Architecture & Selection

### Why Llama 3.2?
I selected **Llama 3.2** as the core engine for this application. The decision was driven by the following factors:

1.  **Efficiency-to-Performance Ratio:** Llama 3.2 offers SOTA reasoning capabilities in the [1B/3B] parameter class, allowing for significantly faster token generation and lower VRAM usage compared to larger models like Llama 3 70B.
2.  **Edge/Cloud Optimization:** The architecture is optimized for efficient hosting on consumer-grade hardware or cost-effective cloud instances (e.g., T4 GPUs or high-end CPUs).
3.  **Embedding Compatibility:** Using Llama 3.2 for semantic embeddings ensures alignment between the retrieval vector space and the generation model, reducing semantic mismatch in RAG pipelines.

### System Architecture
The system follows a modular pipeline:
1.  **Input Processing:** Request validation via Pydantic.
2.  **Embedding Layer:** Input text is vectorized using Llama 3.2.
3.  **Inference Engine:** The core Llama 3.2 model processes the context and generates the response.
4.  **API Layer:** Served via FastAPI for request handling.

---

## ⚡ Performance & Limitations

### Performance Optimizations
* **Quantization:** The model works with quantization to minimize memory footprint without significant degradation in reasoning quality.
* **Caching:** Semantic caching is implemented to store frequently asked queries, reducing GPU load.
* **Concurrency:** Asynchronous non-blocking endpoints allow for handling multiple requests simultaneously.

### Limitations
* **Context Window:** The model is limited to [128k/8k] context length. Inputs exceeding this will be truncated.
* **Knowledge Cutoff:** The model's internal knowledge is limited to its training data cutoff; it does not have real-time internet access unless provided via context.
* **Hardware Dependencies:** While optimized, performance scales heavily with available GPU memory/CUDA cores.

---

## 🛠️ Setup Instructions

Follow these steps to get the API running locally.

### Prerequisites
* Python 3.10 or higher
* Ollama installed
* Llama 3.2 Model pulled locally

### 1. Clone the Repository
```bash
git clone [https://github.com/](https://github.com/)berlyand25/API-AI-Scraper.git
cd [repo-name]
```
### 2. Create a Virtual Environment
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
uvicorn main:app --reload
```

## 📡 API Documentation

## 🎥 Demo
[![Watch the demo](thumbnail.png)](https://drive.google.com/file/d/1xJf9YGKTjJs6Bx593eDgWxAJJemvAcSR/view?usp=sharing)

## 🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request.
