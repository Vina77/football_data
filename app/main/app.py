from flask import Flask, render_template
import io
import base64
import matplotlib.pyplot as plt

from collect import get_match_data
from process import process_data
from visualize import plot_scores 


app = Flask(__name__)

# Substitua "SUA_CHAVE_DE_API" pela sua chave real
api_key = "YOUR_API_KEY"

@app.route('/')
def index():
    # Obter e processar os dados
    data = get_match_data(api_key)
    df = process_data(data)

    # Criar gráfico e convertê-lo para formato que pode ser exibido no HTML
    img = io.BytesIO()
    plot_scores(df, img)
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return render_template('index.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)