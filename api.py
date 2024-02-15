from flask import Flask, request
import json
import os
from supabase import create_client

app = Flask(__name__)

@app.route('/')
def homepage():
    return "API sendo executada"

@app.route('/produto-historico/<product_id>', methods=['GET'])
def get_product(product_id):
    if request.method == 'GET':
        url = os.environ.get("SUPABASE_URL")
        key = os.environ.get("SUPABASE_KEY")
        Client = create_client(url, key)
        
        response = Client.table('Product').select("Nome, link, Product_History!inner(dia, preco, avista, parcelado)").eq("id", product_id).execute()
        re = {
            "Nome": response.data[0]["Nome"],
            "Link": response.data[0]["link"],
            "Historico": response.data[0]['Product_History']
        }
        return json.dumps(re, ensure_ascii=False, indent=2)
app.run(host='0.0.0.0')