def format_docs_with_sources(
        docs
):
    context=""
    for doc in docs:
        context+=f"""
[{doc.metadata["source"]}]

[{doc.metadata['clause']}]
{doc.page_content}
"""
    return context