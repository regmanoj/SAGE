#retriever.py
from sentence_transformers import SentenceTransformer
import pandas as pd
from typing import List, Tuple
from .config import Config
from .utils import load_data, preprocess_text
import chromadb

class Retriever:
    def __init__(self):
        # Initialize the SentenceTransformer model
        self.embedder = SentenceTransformer(Config.EMBEDDING_MODEL)
        
        # Initialize ChromaDB client
        self.client = chromadb.Client()  # No settings needed for the new client
        self.collection = self.client.create_collection("gita_yoga_collection")
        
        self.initialize_knowledge_base()  # Call to initialize the knowledge base

    def initialize_knowledge_base(self):
        # Load and combine data
        gita_df = load_data(Config.GITA_VERSES)
        yoga_df = load_data(Config.YOGA_VERSES)

        # Print the columns to debug
        print("Gita DataFrame Columns:", gita_df.columns.tolist())
        print("Yoga DataFrame Columns:", yoga_df.columns.tolist())

        # Prepare texts for embedding
        gita_texts = [
            f"Chapter {row['Chapter']} Verse {row['Verse']}: {row['Sanskrit ']}" 
            for _, row in gita_df.iterrows()
        ]
        yoga_texts = [
            f"Sutra {row['Verse']}: {row['Word Meanings']}" 
            for _, row in yoga_df.iterrows()
        ]

        # Combine texts from both datasets
        self.texts = gita_texts + yoga_texts

        # Create embeddings
        embeddings = self.embedder.encode(self.texts).tolist()  # Convert to list for ChromaDB

        # Generate unique IDs for each document
        ids = [str(i) for i in range(len(self.texts))]  # Simple numeric IDs

        # Add documents and embeddings to ChromaDB
        self.collection.add(documents=self.texts, embeddings=embeddings, ids=ids)

    def get_relevant_context(self, query: str, k: int = Config.TOP_K) -> List[Tuple[str, float]]:
        # Encode the query to get its vector representation
        query_vector = self.embedder.encode([query]).tolist()  # Convert to list for ChromaDB
        
        # Query ChromaDB for the most similar documents
        results = self.collection.query(query_embeddings=query_vector, n_results=k)  # Use query_embeddings instead of embeddings
        
        # Extract the texts and their corresponding distances
        texts = results['documents'][0]
        distances = results['distances'][0]

        # Prepare the results
        return [(text, 1 - distance) for text, distance in zip(texts, distances)]