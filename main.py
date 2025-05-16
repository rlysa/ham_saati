from flask import Flask, render_template, request, redirect, url_for, session
#from saati_algorithm import ham_saati

app = Flask(__name__)
app.secret_key = 'change_this_to_a_random_secret'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/input', methods=['GET', 'POST'])
def input_data():
    if request.method == 'POST':
        session['criteria_count'] = int(request.form['criteria_count'])
        session['alt_count'] = int(request.form['alt_count'])
        return redirect(url_for('input_names'))
    return render_template('input_data.html')


@app.route('/names', methods=['GET', 'POST'])
def input_names():
    c = session.get('criteria_count')
    a = session.get('alt_count')
    if not c or not a:
        return redirect(url_for('input_data'))

    if request.method == 'POST':
        crit_names = request.form.getlist('criteria_names')
        alt_names  = request.form.getlist('alt_names')
        session['criteria_names'] = crit_names
        session['alt_names'] = alt_names
        return redirect(url_for('compare_criteria'))
    return render_template('criteria_names.html',
                           criteria_count=c,
                           alt_count=a)


@app.route('/compare_criteria', methods=['GET', 'POST'])
def compare_criteria():
    crit_names = session.get('criteria_names')
    if request.method == 'POST':
        return redirect(url_for('compare_objects'))
    return render_template('compare_criteria.html',
                           criteria_names=crit_names)


@app.route('/compare_objects', methods=['GET', 'POST'])
def compare_objects():
    crit_names = session.get('criteria_names')
    alt_names  = session.get('alt_names')
    if request.method == 'POST':
        return redirect(url_for('results'))
    return render_template('compare_objects.html',
                           criteria_names=crit_names,
                           alt_names=alt_names)


@app.route('/results')
def results():
    crit_names = session.get('criteria_names')
    alt_names  = session.get('alt_names')
    crit_matrix = session.get('criteria_matrix')
    obj_matrices = session.get('objects_matrices')

    result = run_saati(
        criteria_names=crit_names,
        alt_names=alt_names,
        crit_matrix=crit_matrix,
        obj_matrices=obj_matrices
    )

    return render_template('results.html',
                           criteria_matrix=result.normalized_criteria_matrix,
                           criteria_names=crit_names,
                           criteria_weights=result.criteria_weights,
                           alt_names=alt_names,
                           final_scores=result.final_scores,
                           sorted_alternatives=result.ranking)


if __name__ == '__main__':
    app.run(debug=True)
