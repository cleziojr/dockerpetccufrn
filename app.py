from flask import Flask
import requests

app = Flask(__name__)

# API gratuita que encontrei
API_URL = "https://api.adviceslip.com/advice"

@app.route('/')
def route():
    try:
        # Fazendo a requisição GET para a API de curiosidade
        response = requests.get(API_URL)
        data = response.json()
        
        # Data é um dicionário que contém um dicionário. Passando as chaves entre colchetes e aspas simples, torna-se possível obter
        # o valor correspondente à curiosidade
        curiosity = data['slip']['advice']
        
        return curiosity
    except Exception as e:
        return f"Erro ao obter curiosidade: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
