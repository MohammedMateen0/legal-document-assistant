from langchain_core.documents import (
    Document
)
import os

def load_documents(folder_path):
    documents=[]
    for file in os.listdir(
        folder_path
    ):
        if file.endswith(
            ".txt"
        ):
            path=os.path.join(
                folder_path,
                file
            )
            with open(
                path,
                "r",
                encoding="utf-8"
            ) as f:
                text=f.read()
            documents.append(
                Document(
                    page_content=text,
                    metadata={
                        "source":file
                    }
                )
            )
    return documents