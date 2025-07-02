# Quotes App

Простое веб-приложение на Flask, которое показывает случайную цитату, используя публичные API:

- [ZenQuotes API](https://zenquotes.io/api/random)
- [API Ninjas Quotes](https://api-ninjas.com/api/quotes)
- [Quoteslate API](https://quoteslate.vercel.app/)

## Как запустить

1. Клонируйте репозиторий или распакуйте ZIP:
   ```
   git clone https://github.com/yourusername/quotes_app.git
   cd quotes_app
   ```

2. Установите зависимости:
   ```
   pip install flask requests
   ```

3. (Необязательно) Получите API ключ с [api-ninjas.com](https://api-ninjas.com) и вставьте его в `app.py` вместо `'your_api_key_here'`.

4. Запустите сервер:
   ```
   python app.py
   ```

5. Откройте в браузере:
   ```
   http://127.0.0.1:5000
   ```

## Структура проекта

```
quotes_app/
├── app.py
├── templates/
│   └── index.html
└── README.md
```

## Пример

![Пример](https://user-images.githubusercontent.com/example/screenshot.png)
