from app import app, loop
from flask import request
from app.models import Docs
from app.tasks import search, delete

@app.get('/search/')
def get_posts():
    text = request.args["text"]
    result = loop.run_until_complete(search(Docs, text))
    return result

@app.delete('/delete/')
def delete_post():
    delete_item = query_index_by_id('docs', id)
    if delete_item != NULL:
        elastic_result = delete_by_id('docs', id)
        if elastic_result is True:
            db_result = bool(Model.query.filter(Model.id==id).delete())
            db.session.commit()
            return str(db_result)
        return "Not found post with such id"
    result = loop.run_until_complete(delete(Docs, id))
    return 
