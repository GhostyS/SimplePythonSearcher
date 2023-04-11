from app import db, es
import app.elastic_methods

def search(Model, text):
    try:

    except Exception:
        return Exception
   
def delete(Model, id):
    delete_item = query_index_by_id('docs', id)
