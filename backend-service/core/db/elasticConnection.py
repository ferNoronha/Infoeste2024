from elasticsearch import Elasticsearch
from config import settings

client = Elasticsearch(
    settings.ELASTIC_URL
    # basic_auth=("elastic", ELASTIC_PASSWORD)
)

print('Connected to Elasticsearch...')
