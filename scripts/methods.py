from app import db, es
from app.elastic import query_index_by_text, query_index_by_id

def search(Model, text):
    for doc in Model.query.all():
        add_to_index('docs', doc)
    if text is None:
        return "Text is None"
    ids = query_index_by_text('docs', text)
    result = Model.query.filter(Model.id.in_(ids)).order_by(Model.created_date.desc()).all()
    return {"result": [doc.as_dict() for doc in result]}
