from flask import Flask, render_template
import pandas as pd
from dotenv import load_dotenv

app = Flask(__name__)

# Carrega o arquivo .env
load_dotenv()

@app.route('/')
def index():
    return render_template('index.html')
    
df = pd.DataFrame({
    'alunos': ['Renato', 'Fernando', 'Rodrigo', 'Ana', 'Joana', 'Silvio', 'Carolina'],
    'notas': [15.00, 39.58, 62.92, 41.46, 48.33, 63.13, 70.00]
})

@app.route('/table')
def table():
    # Renderiza o html na tela com os dados das notas
    return render_template('table.html', notas=[df.to_html(classes='data')])

if __name__ == '__main__':
    # Aplica o Flask na porta 5000
    app.run(port=5000)