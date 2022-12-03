from flask import jsonify
from flask import Flask, request
from nltk.util import ngrams
from nltk import word_tokenize

app = Flask(__name__)

def get_ngrams(text, n):
    n_grams = ngrams(word_tokenize(text), n)
    return [' '.join(grams) for grams in n_grams]

@app.route('/')
def home():
    return ''

@app.route('/get_ngrams', methods=['POST'])
def query():
    data = request.get_json()
    text = data["text"]
    n = data["n"]
    ngram_list = get_ngrams(text, n)
    return jsonify(output = ngram_list)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8080)