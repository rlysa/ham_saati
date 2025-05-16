from flask import Flask, render_template, request, redirect, url_for, session
#from saati_algorithm import run_saati

app = Flask(__name__)
app.secret_key = 'your_secret_key'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/input', methods=['GET', 'POST'])
def input_data():
    if request.method == 'POST':
        session['criteria_count'] = int(request.form['criteria_count'])
        session['object_count'] = int(request.form['object_count'])
        return redirect(url_for('criteria_names'))
    return render_template('input_data.html')


@app.route('/criteria', methods=['GET', 'POST'])
def criteria_names():
    if request.method == 'POST':
        criteria_names = [request.form[f'crit_{i}'] for i in range(session['criteria_count'])]
        session['criteria_names'] = criteria_names
        return redirect(url_for('compare_criteria'))
    return render_template('criteria_names.html', count=session['criteria_count'])


@app.route('/compare_criteria', methods=['GET', 'POST'])
def compare_criteria():
    pass


@app.route('/input_objects', methods=['GET', 'POST'])
def input_objects():
    pass


@app.route('/compare_objects', methods=['GET', 'POST'])
def compare_objects():
    pass


@app.route('/results')
def results():
    return render_template('results.html', result=calculated_data)


if __name__ == "__main__":
    app.run()
