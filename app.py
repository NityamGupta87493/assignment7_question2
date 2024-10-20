from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('register'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_id = request.form['userid']
        password = request.form['password']
        # Normally, here you would add logic to store the user credentials securely
        # For this example, we'll just print them to the console
        print(f'Registered UserID: {user_id}, Password: {password}')
        return 'Registration successful!'
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
