from flask import Flask, render_template, request, redirect, url_for, session
from saati_algorithm import run_saati

app = Flask(__name__)
app.jinja_env.globals.update(zip=zip)

app.secret_key = 'your_secret_key'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/input', methods=['GET', 'POST'])
def input_data():
    if request.method == 'POST':
        session['criteria_count'] = int(request.form['criteria_count'])
        session['alt_count']      = int(request.form['alt_count'])

        return redirect(url_for('compare_criteria'))

    return render_template('input_data.html')


@app.route('/compare_criteria', methods=['GET','POST'])
def compare_criteria():
    form = request.form
    if request.method == 'POST' and 'criteria_count' in form:
        session['criteria_count']  = int(form['criteria_count'])
        session['alt_count']       = int(form['alt_count'])
        session['criteria_names']  = form.getlist('criteria_names')
        session['alt_names']       = form.getlist('alt_names')
        return redirect(url_for('compare_criteria'))

    crit_names = session.get('criteria_names')
    c = session.get('criteria_count')
    if not crit_names or not c:
        return redirect(url_for('input_data'))

    if request.method == 'POST' and 'criteria_count' not in form:
        matrix = [[1.0]*c for _ in range(c)]
        for i in range(c):
            for j in range(i+1, c):
                val = float(form[f'comp_{i}_{j}'])
                matrix[i][j] = val
                matrix[j][i] = 1.0/val
        session['criteria_matrix'] = matrix
        return redirect(url_for('compare_objects'))

    return render_template('compare_criteria.html',
                           criteria_names=crit_names)


@app.route('/compare_objects', methods=['GET', 'POST'])
def compare_objects():
    crit_names = session['criteria_names']
    alt_names  = session['alt_names']
    c = len(crit_names)
    a = len(alt_names)

    if request.method == 'POST':
        all_mats = []
        for k in range(c):
            mat = [[1.0]*a for _ in range(a)]
            for i in range(a):
                for j in range(i+1, a):
                    val = float(request.form[f'obj_{k}_{i}_{j}'])
                    mat[i][j] = val
                    mat[j][i] = 1/val
            all_mats.append(mat)
        session['objects_matrices'] = all_mats
        return redirect(url_for('results'))

    return render_template('compare_objects.html',
                           criteria_names=crit_names,
                           alt_names=alt_names)



@app.route('/results')
def results():
    crit_names  = session['criteria_names']
    alt_names   = session['alt_names']
    crit_matrix = session['criteria_matrix']
    obj_matrices= session['objects_matrices']

    res = run_saati(
        criteria_names=crit_names,
        alt_names=alt_names,
        crit_matrix=crit_matrix,
        obj_matrices=obj_matrices
    )

    return render_template('results.html',
        criteria_matrix=res.normalized_criteria_matrix,
        criteria_names=crit_names,
        criteria_weights=res.criteria_weights,
        alt_names=alt_names,
        final_scores=res.final_scores,
        sorted_alternatives=res.ranking
    )


if __name__ == '__main__':
    app.run(debug=True)
