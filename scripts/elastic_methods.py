import elasticsearch
from app import el_s

def delete_by_id(index, id):
    try:
        el_s.delete(index=index, id=id)
        return True
    except elasticsearch.NotFoundError:
       return False

def query_index_by_text(index, text):
    search = es.search(
        index=index,
        size=20,
        query = { 'multi_match': {'query': text, 'fields': ['*']}, "sort": [{"date_field": {"order": "desc"}}]})
    ids = [int(hit['_id']) for hit in search['hits']['hits']]
    return ids
      
    

def get_doc_by_id(index, id):
    return True
    
    
