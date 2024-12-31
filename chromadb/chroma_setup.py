import chromadb
from chromadb.config import Settings
def initialize_chroma():
    client=chromadb.Client(Settings(
        persist_directory="./chromadb/chroma_data",
        chroma_db_imple="duckdb+parquet"
    ))
    collection=client.create_collection("training_docs")
    return client, collection