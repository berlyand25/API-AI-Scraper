import json
import time

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from langchain_core.vectorstores import InMemoryVectorStore
from scraper_utils import (
    embeddings,
    load_page, 
    split_text, 
    index_docs, 
    retrieve_docs, 
    answer_question,
)

app = FastAPI()

class Item(BaseModel):
    url: str
    query: str

@app.get('/')
def root():
    return {"message" : "Welcome to the AI Web Scraper API!"}

@app.post('/parse')
def parse_url(item: Item):
    start_time = time.time()

    vector_store = InMemoryVectorStore(embeddings)

    documents = load_page(item.url)
    chunk_documents = split_text(documents)
    index_docs(chunk_documents, vector_store)

    retrieved_documents = retrieve_docs(item.query, vector_store)
    context = "\n\n".join([doc.page_content for doc in retrieved_documents])
    answer = answer_question(item.query, context)

    try:
        data = json.loads(answer)
    except:
        raise HTTPException(status_code=500, detail='Failed to parse LLM response as JSON')
    
    end_time = time.time()
    duration_ms = (end_time - start_time) * 1000

    if len(data) == 0:
        raise HTTPException(status_code=404, detail='No data found for the given query')

    return {
        "result" : data,
        "message" : "Found {} record(s)".format(len(data)),
        "metadata": {
            "processing_time_ms": round(duration_ms)
        }
    }