from elasticsearch import Elasticsearch, helpers
import json



es = Elasticsearch([{'host': 'localhost', 'port':9200}])

def data_upload():
    with open('director-corpus/directors_tamil.json') as f:
        data = json.loads(f.read())
    helpers.bulk(es, data, index='index-directors', doc_type='famous-directors')


if __name__ == "__main__":
    data_upload()

