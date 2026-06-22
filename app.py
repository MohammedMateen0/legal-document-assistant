import streamlit as st

from setup import build_system

@st.cache_resource
def load_system():
    return build_system()

retriever,rag_chain,rewriter=(
    load_system()
)
st.set_page_config(
    page_title="Legal Document Assistant",
    page_icon="⚖️"
)
st.title(
    "⚖️ Legal Document Assistant"
)

st.write(
    "Ask questions about legal documents."
)

query=st.chat_input(
    "Ask a legal Question..."
)
if query:

    rewritten_query = (
        rewriter.rewrite(
            query
        )
    )

    docs = retriever.invoke(
        rewritten_query
    )

    answer = rag_chain.invoke(
        rewritten_query
    )

    with st.chat_message(
        "user"
    ):
        st.write(
            query
        )

    with st.chat_message(
        "assistant"
    ):
        st.write(
            answer
        )

        with st.expander(
            "Sources"
        ):

            for doc in docs:

                st.markdown(
                    f"""
**Document**
{doc.metadata.get('source')}

**Clause**
{doc.metadata.get('clause')}
"""
                )

                st.write(
                    doc.page_content
                )

                st.divider()