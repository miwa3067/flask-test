from flask import Flask, render_template, request

app = Flask(__name__)

# getのときの処理


@app.route('/', methods=['GET'])
def get():
    return render_template('index.html',
                           title='Form Sample(get)',
                           message='名前を入力して下さい。',
                           password='')

# postのときの処理


@app.route('/', methods=['POST'])
def post():
    name = request.form['name']
    pw1 = request.form['password']
    pw2 = request.form['password2']
    return render_template('index.html',
                           title='Form Sample(post)',
                           message='こんにちは、{}さん, pw:{}, pw2:{}'.format(name, pw1, pw2))


if __name__ == '__main__':
    app.run(debug=True)
