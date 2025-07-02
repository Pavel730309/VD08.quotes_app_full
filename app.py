from flask import Flask, render_template
import requests
import random

app = Flask(__name__)

def get_quote():
    # Список публичных API
    apis = [
        "https://zenquotes.io/api/random",
        "https://api.api-ninjas.com/v1/quotes",
        "https://quoteslate.vercel.app/api/quote"
    ]

    selected_api = random.choice(apis)

    headers = {}
    if "api-ninjas" in selected_api:
        headers = {
            'X-Api-Key': 'your_api_key_here'  # ← Вставь свой API ключ от api-ninjas.com
        }

    try:
        response = requests.get(selected_api, headers=headers)
        data = response.json()

        # Разные API — разный формат
        if "zenquotes" in selected_api:
            quote = data[0]['q']
            author = data[0]['a']
        elif "api-ninjas" in selected_api:
            quote = data[0]['quote']
            author = data[0]['author']
        elif "quoteslate" in selected_api:
            quote = data['quote']
            author = data['author']
        else:
            quote = "Цитата не найдена"
            author = ""

        return quote, author
    except Exception as e:
        return "Ошибка при получении цитаты", str(e)

@app.route('/')
def index():
    quote, author = get_quote()
    return render_template('index.html', quote=quote, author=author)

if __name__ == '__main__':
    app.run(debug=True)
