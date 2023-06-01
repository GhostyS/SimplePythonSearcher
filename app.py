from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from elasticsearch import Elasticsearch
import asyncio

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)
es = Elasticsearch('http://elastic:9200')
loop = asyncio.new_event_loop()

"""
if __name__ == "__main__":
    #with app.app_context():
    #    db.create_all()
    doc = {'title': 'My Document', 'content': 'Some content'}
    es.index(index='my_index', document=doc)
    app.run(debug=True)"""
import routes, models
