from langchain_community.document_loaders import PlaywrightURLLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

MODEL_NAME = "llama3.2"
embeddings = OllamaEmbeddings(model=MODEL_NAME)
model = OllamaLLM(model=MODEL_NAME)

template = """
You are a strict Data Extraction Engine.
You will receive a user question and a set of retrieved contexts.

Your task:
1. If the answer to the question can be found in the retrieved context:
   - Respond strictly in JSON format.
   - The JSON must be a list of objects.
   - Each object should contain the extracted fields relevant to the question.
   - Do not add explanations, metadata, or text outside the JSON.
   - Extract all available data points that match the user's request

2. If the answer cannot be found in the retrieved context:
   - Do not guess or fabricate information.
   - Respond with an empty JSON list: []

Rules:
- Never hallucinate fields that are not explicitly available in the context.
- If a field is missing in the text, set the value to null or omit the field.
- Preserve all numeric values, text, and lists exactly as they appear.

Question: {question}
Context: {context}
Answer:
"""

def load_page(url):
    loader = PlaywrightURLLoader(
        urls=[url],
        headless=True,
        continue_on_failure=True
    )
    documents = loader.load()

    return documents

def split_text(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=2500,
        chunk_overlap=250,
        separators=["\n\n", "\n", " ", ""],
        add_start_index=True
    )
    texts = text_splitter.split_documents(documents)

    return texts

def index_docs(documents, vector_store):
    vector_store.add_documents(documents)

def retrieve_docs(query, vector_store):
    return vector_store.similarity_search(query, k=10)

def answer_question(question, context):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    return chain.invoke({
        "question": question,
        "context": context
    })