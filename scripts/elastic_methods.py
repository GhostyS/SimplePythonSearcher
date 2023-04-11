import elasticsearch
from app import el_s

def delete_by_id(index, id):
    try:
        el_s.delete(index=index, id=id)
        return True
    except elasticsearch.NotFoundError:
       return False

def get_id_by_text(index, text):
    

def get_doc_by_id(index, id):
    
    
