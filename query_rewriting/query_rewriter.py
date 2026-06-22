from langchain_ollama import (
    ChatOllama
)
from langchain_core.prompts import (
    ChatPromptTemplate
)
from langchain_core.output_parsers import (
    StrOutputParser
)

class QueryRewrite:
    def __init__(self):
        self.llm=ChatOllama(
            model="llama3.2",
            temperature=0
        )
        self.prompt=(
            ChatPromptTemplate.from_template(
                """
You are part of a Retrieval-Augmented Generation (RAG) system.

Your job is NOT to answer the user's question.

Your job is to convert the user's question into a search query that will help a document retriever find the most relevant legal document sections.

The retriever searches legal contracts, agreements, policies, and clauses.

A good rewritten query should:

- Contain the important legal concepts.
- Be more specific than the user's original question.
- Help semantic search retrieve the correct document section.
- Preserve the original meaning.
- Never answer the question.
- Never invent facts.
- Never add information not implied by the question.
- Use the examples only as references for style and behavior.
- Do NOT copy words, topics, or phrasing from the examples unless they are relevant to the user's question.
- Generate the rewritten query based on the user's actual question.

Return ONLY the rewritten query.

Examples:

Question:
notice period

Rewritten Query:
What is the notice period for employment termination?

Question:
nda duration

Rewritten Query:
How long does the non-disclosure agreement remain effective?

Question:
health insurance

Rewritten Query:
Who is eligible for health insurance coverage?

Question:
termination

Rewritten Query:
Under what conditions can the agreement be terminated?

Question:
{query}

Rewritten Query:
"""
            )
        )
        self.chain=(
            self.prompt
            | self.llm
            | StrOutputParser()
        )
    def rewrite(
            self,
            query
    ):
        return (self.chain.invoke(
            {
                "query":query
            }
        ).strip()
    )