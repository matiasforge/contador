from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 1
    return render_template('index.html', visits=session['visits'])

@app.route('/destroy_session')
def destroy_session():
    session.pop('visits', None)
    return redirect(url_for('index'))

@app.route('/increment_by_2')
def increment_by_2():
    if 'visits' in session:
        session['visits'] += 2
    else:
        session['visits'] = 2
    return redirect(url_for('index'))

@app.route('/reset_counter')
def reset_counter():
    session['visits'] = 0
    return redirect(url_for('index'))

@app.route('/increment', methods=['GET', 'POST'])
def increment():
    if request.method == 'POST':
        increment_value = int(request.form['increment_value'])
        if 'visits' in session:
            session['visits'] += increment_value
        else:
            session['visits'] = increment_value
        return redirect(url_for('index'))
    return render_template('increment.html')

if __name__ == '__main__':
    app.run(debug=True)
