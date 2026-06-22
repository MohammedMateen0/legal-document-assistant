import re

def enrich_metadata(chunks):
    for chunk in chunks:
        text=chunk.page_content
        clause="Unknown"
        
        match = re.search(
            r"SECTION\s+\d+:\s+([^\n]+)",
            text
        )
        if match:
            clause=match.group()
        chunk.metadata["clause"]=clause
    return chunks