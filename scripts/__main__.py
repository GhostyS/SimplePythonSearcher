from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from elasticsearch import Elasticsearch
import asyncio

app = Flask(__name__)
app.config.from_object(Config)
el_s = Elasticsearch('http://elastic:9200')
