# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 17:27:24 2026

@author: user
"""
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_classic.chains import RetrievalQAWithSourcesChain
from uuid import uuid4
from pathlib import Path

load_dotenv()
CHUNK_SIZE = 100
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"  #embedding
VECTORSTORE_DIR = Path(__file__).parent / "resources/vectorstore"
COLLECTION_NAME = "real_estate"
FOLDER_PATH = Path(__file__).parent / "docs/debug.log"

llm = None
vector_store = None
def initialize_components():
    
    global llm,vector_store
    if llm is None:
        llm = ChatGroq(model_name="llama-3.1-8b-instant", temperature=0.9, max_tokens=500) #Large language model
    if vector_store is None:
        ef = HuggingFaceEmbeddings(
            model_name = EMBEDDING_MODEL,
            model_kwargs = {"trust_remote_code":True}
            )
        vector_store = Chroma(
            collection_name = COLLECTION_NAME,
            embedding_function = ef,
            persist_directory = str(VECTORSTORE_DIR)
            )

        


def process_docs():
    yield "Initialize components..."
    initialize_components()
    
    yield "Resetting vector db ..."
    if vector_store._collection.count() > 0:
        vector_store.reset_collection()
   
    
    yield "Load data..."
    
    loader = TextLoader(FOLDER_PATH)
    documents = loader.load()
    
    print("Len is ", len(documents))
    
    yield "Split text..."
    text_splitter = RecursiveCharacterTextSplitter(
        separators = ["\n\n","\n","."," "],
        chunk_size = 2000,
        chunk_overlap = 200
        )
    docs = text_splitter.split_documents(documents)
    
    yield "Add docs to vector db ..."
    uuids = [str(uuid4()) for _ in range(len(docs))]
    vector_store.add_documents(docs, ids=uuids)
    
    yield "Done adding docs to vector database"
def search(query):
    if not vector_store:
        raise RuntimeError("Vector db is not initialised")
    chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vector_store.as_retriever())
    result = chain.invoke({"question": query}, return_only_outputs=True)
    return result["answer"]
    
    
    
    
