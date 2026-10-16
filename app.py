from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Главная')

@app.route('/about')
def about():
    return render_template('about.html', title='О нас')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    message = None
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        text = request.form.get('message', '').strip()
        if name and text:
            message = f'Спасибо, {name}! Ваше сообщение получено.'
        else:
            message = 'Пожалуйста, заполните все поля.'
    return render_template('index.html', title='Контакты', message=message)

if __name__ == '__main__':
    app.run(debug=True)