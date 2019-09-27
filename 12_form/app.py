#Jesse "McCree" Chen and Ivan Galakhov
#SoftDev1 pd1
#K12 -- Echo Echo Echo
#2019-09-27


from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    # print([i for i in request.form.values()])
    # print(request.form['first'])
    # print(request.form['last'])
    # print(request.form['moment'])

    return render_template('index.html')


@app.route('/auth', methods=['GET', 'POST'])
def auth():
    return render_template('auth.html',
                           request=request)


if __name__ == '__main__':
    app.run(debug=True)
