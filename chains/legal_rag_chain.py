from langchain_ollama import (
    ChatOllama
)
from langchain_core.output_parsers import (
    StrOutputParser
)
from langchain_core.runnables import (
    RunnablePassthrough
)
from chains.prompts import (
    LEGAL_PROMPT
)
from utils.format_docs import (
    format_docs_with_sources
)
def create_legal_rag_chain(
        retriever
):
    llm=ChatOllama(
        model="llama3.2",
        temperature=0
    )
    chain=(
        {
        "context":
        retriever
        | format_docs_with_sources,
        "question":
        RunnablePassthrough()
    }
    | LEGAL_PROMPT
    | llm
    | StrOutputParser()
    )
    return chain