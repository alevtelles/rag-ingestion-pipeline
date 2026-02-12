import os
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv

load_dotenv()



def load_documents(docs_path="docs"):
    """
        Carrega todos os arquivos do diretório docs
    """
    print(f"Carrregando documentos do diretório {docs_path}")
    
    # Checar se o diretório de documentos existe
    if not os.path.exists(docs_path) :
        raise FileNotFoundError(f"O diretório {docs_path} não existe. Por favor, crie-o e adicione os arquivos da sua empresa.")

    # Carregar todos os arquivos .txt que estão no diretório docs
    loader = DirectoryLoader(
        path=docs_path,
        glob="*.txt",
        loader_cls=TextLoader
    )

    documents = loader.load()

    if len(documents) == 0:
        raise FileNotFoundError(f"Nenhum arquivo .txt foi encontrado em {docs_path}. Por favor, adicione os documentos da sua empresa.")
    
    for i, doc in enumerate(documents[:2]):
        print(f"\nDocument {i+1}:")
        print(f" Source: {doc.metadata['source']}")
        print(f" Content: length{len(doc.page_content)} characteres")
        print(f" Content: preview {doc.page_content[:100]}...")
        print(f" metadata: {doc.metadata}")
    
    return documents


def slipt_documents(documents, chunk_size=800, chunk_overlap=0):
    """Split documents into smaller chucks with overlap"""
    print("Splitting docucuments into chunks...")


    text_splitter = CharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    chunks = text_splitter.split_documents(documents)

    if chunks:

        for i, chunk in enumerate(chunks[:5]):
            print(f"\n--- Chunk {i+1} ---")
            print(f" Source: {chunk.metadata['source']}")
            print(f" Length: {len(chunk.page_content)} characteres")
            print(f" Content:")
            print(f"{chunk.page_content}")
            print("-" * 50)

            if len(chunks) > 5:
                print(f"\n... and {len(chunks) -5} more chunks")
        
        return chunks
    

def create_vector_store(chunks, persist_directory="db/chroma_db"):
    """Create and persist ChromaDB vector store"""
    print("Creating embeddings and storing in ChromaDB...")

    embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")

    # Create ChromaDB vector store
    print("--- CREATING VECTOR STORE ---")
    vectorstore= Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model, 
        persist_directory=persist_directory,
        collection_metadata={"hnsw:space": "cosine"}
    )

    print("--- Finished creating vector store ---")

    print(f"Vector store created and saved to {persist_directory}")
    return vectorstore


def main():
    print("Main Function")

    # Carregar os arquivos
    documents = load_documents(docs_path="docs")

    # Fazer os chinkig dos arquivos
    chunks = slipt_documents(documents)

    # Embedings e armazenar no banco vetorial
    vectorstore = create_vector_store(chunks)


if __name__ == "__main__":
    main()