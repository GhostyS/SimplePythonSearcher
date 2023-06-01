from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from elasticsearch import Elasticsearch

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)
migrate = Migrate(app, db)
es = Elasticsearch('http://elastic:9200')


from app import routes, models
