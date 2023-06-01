from app import app, db, es
from flask import request
from app.models import Docs
from app.elastic import delete_by_id, query_index_by_text, query_index_by_id, add_to_index

def search(Model, text):
    if not es.indices.exists(index='docs'):
        for post in Model.query.all():
            add_to_index('docs', post)
    if text is None:
        return "Text is None"
    try:
        ids = query_index_by_text('docs', text)
        result = Model.query.filter(Model.id.in_(ids)).order_by(Model.created_date.desc()).all()
        return {"result": [post.as_dict() for post in result]}
    except Exception as exc:
        return str(exc)

def delete(Model, id):
    if not es.indices.exists(index='docs'):
        for post in Model.query.all():
            add_to_index('docs', post)
    delete_item = query_index_by_id('docs', id)
    if delete_item is not None:
        elastic_result = delete_by_id('docs', id)
        if elastic_result is True:
            db_result = bool(Model.query.filter(Model.id==id).delete())
            db.session.commit()
            return str(db_result)
        return "Not found "
    return "Not found "

@app.get('/search/')
def get_posts():
    text = request.args["text"]
    result = search(Docs, text)
    return result

@app.delete('/delete/')
def delete_post():
    id = request.args["id"]
    result = delete(Docs, id)
    return result

