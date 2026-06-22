import re
from langchain_core.documents import Document


def split_documents(documents):

    chunks = []

    for doc in documents:

        sections = re.split(
            r"(?=SECTION\s+\d+:)",
            doc.page_content
        )

        for section in sections:

            section = section.strip()

            if section:

                chunks.append(
                    Document(
                        page_content=section,
                        metadata=doc.metadata.copy()
                    )
                )

    return chunks