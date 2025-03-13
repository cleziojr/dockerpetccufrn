from flask import Flask
import requests

app = Flask(__name__)

# Exemplo de URL de uma API de curiosidade do dia
API_URL = "https://api.adviceslip.com/advice"  # Substitua por uma API real de curiosidade

@app.route('/')
def route():
    try:
        # Fazendo a requisição GET para a API de curiosidade
        response = requests.get(API_URL)
        data = response.json()
        
        # Aqui estamos assumindo que a API retorna um campo 'content' com a curiosidade
        curiosity = data['slip']['advice']
        
        return curiosity
    except Exception as e:
        return f"Erro ao obter curiosidade: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
