from flask import Flask, render_template,request
from elasticsearch import Elasticsearch

app= Flask(__name__)
es =  Elasticsearch()

@app.route('/', methods=["GET", "POST"])
def home():

    q = request.form.get("q")

    if q is not None:
        resp = es.search(index="articulos", doc_type="_doc", body={"query": {"prefix": {"title": q}}})
        return render_template('home.html', q=q, response=resp)
    
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)