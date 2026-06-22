from query_rewriting.query_rewriter import QueryRewrite

rewriter=QueryRewrite()
query=input("Qution: ")

print("\n Rewritten Query:\n")
print(
    rewriter.rewrite(
        query
    )
)