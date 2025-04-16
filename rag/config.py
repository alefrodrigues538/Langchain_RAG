import os
from dotenv import load_dotenv

load_dotenv()

COHERE_API_KEY = os.getenv("COHERE_API_KEY")
DATA_PATH = "data/documents"
INDEX_PATH = "embeddings/chroma_index"
