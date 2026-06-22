from loaders.document_loader import (
    load_documents
)
from splitters.legal_splitter import (
    split_documents
)
from metadata.enrich_metadata import (
    enrich_metadata
)
from embeddings.embedding_model import (
    get_embeddings
)
from vectorstore.chroma_store import (
    create_vectorstore
)
from retrieval.retriever import (
    create_retriver
)
from chains.legal_rag_chain import (
    create_legal_rag_chain
)
from query_rewriting.query_rewriter import (
    QueryRewrite
)

documents=load_documents(
    "data"
)
print(f"\nDocuments Loaded: {len(documents)}")

chunks=split_documents(
    documents
)
chunks=enrich_metadata(
    chunks
)

print(f"Chunks Created: {len(chunks)}")
embeddings=get_embeddings()
vectorstore=create_vectorstore(
    chunks,
    embeddings
)
retriever=create_retriver(
    vectorstore
)
rag_chain=create_legal_rag_chain(
    retriever
)
query=input("\nQuestion: ")
rewriter=QueryRewrite()

rewritten_query=rewriter.rewrite(
    query
)
print(f"\nRewritten Query: \n{rewritten_query}")



answer=rag_chain.invoke(rewritten_query)
print("\nAnswer: \n")
print(answer)