from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


class RAG:
    def __init__(self):
        self.db = None

    def load_pdf(self, file_path):
        loader = PyPDFLoader(file_path)
        docs = loader.load()

        splitter = RecursiveCharacterTextSplitter(chunk_size=500)
        chunks = splitter.split_documents(docs)

        embeddings = HuggingFaceEmbeddings()

        self.db = FAISS.from_documents(chunks, embeddings)

    def query(self, question):
        if not self.db:
            return "No PDF loaded."

        docs = self.db.similarity_search(question)
        return docs[0].page_content