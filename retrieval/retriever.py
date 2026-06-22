def create_retriver(
        vectorstore
):
    return vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k":4,
            "fetch_k":20
        }
    )