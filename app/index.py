import numpy as np
from flask import Flask, request, jsonify
import pickle
import os


app = Flask(__name__)

modelo = pickle.load(open('pipeline_model_gbc_v1.pkl','rb'))

# "jsonfy" é utilizado no lugar de pickle.dump(data, file)

@app.route('/')
def verifica_api_online():
    return "API ONLINE v1.0", 200

@app.route('/predict', methods=['POST'])
def predict():
    dados = request.get_json(force=True)
    predicao = modelo.predict(np.array([list(dados.values())]))
    resultado = predicao[0]

    resposta = {'DIABETES', int(resultado)}
    return jsonify(resposta)

if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(host='0.0.0.0',port=port) #debug=True