import chromadb

chroma_client = chromadb.PersistentClient( path = 'chroma_db' )
collection = chroma_client.get_collection( name = 'SkillsDynamix_About_Us' )


def get_relevant_chunks(  user_query: str) -> list[ str ] :
    
    results = collection.query(
    query_texts= [ user_query ],
    n_results= 1
    )
    
    return results['documents']