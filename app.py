from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Задание: вывести в консоль
    print("\n" + "="*30)
    print("НОВОЕ СООБЩЕНИЕ ИЗ ФОРМЫ:")
    print(f"Имя: {name}")
    print(f"Email: {email}")
    print(f"Сообщение:\n{message}")
    print("="*30 + "\n")

    # Возвращаем пользователя на главную (можно добавить flash-сообщение)
    return render_template('index.html', success=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
