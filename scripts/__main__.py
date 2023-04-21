from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from elasticsearch import Elasticsearch

app = Flask(__name__)
el_s = Elasticsearch('http://elastic:9200')
print(app)

