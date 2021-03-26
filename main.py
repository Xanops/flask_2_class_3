from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/list_prof/<list>')
def loop(list):
    sp = ['инженер-исследователь', "пилот", "строитель", "экзобиолог", "врач", "инженер по терраформированию",
          "климатолог", "специалист по радиационной защите", "астрогеолог", "гляциолог", "инженер  жизнеобеспечиния",
          "метеоролог", "оператор марсохода", "киберинженер", "штурман", "пилот дронов"]
    if list == 'ol':
        return render_template('sp.html', arg=list, sp=sp)
    elif list == 'ul':
        return render_template('sp.html', arg=list, sp=sp)
    else:
        return render_template('sp.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
