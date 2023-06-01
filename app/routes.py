from app import app
from flask import request
from app.models import Docs
from app.tasks import search, delete

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

