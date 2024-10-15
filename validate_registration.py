from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def registration_form():
    return render_template('registration.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

    # Basic validation
    if not (username and email and password and confirm_password):
        return "All fields are required!"

    if password != confirm_password:
        return "Passwords do not match!"

    # Here you would typically save the user data to a database or perform further actions

    return f"Registration successful for {username} with email {email}!"

if __name__ == '__main__':
    app.run(debug=True)
