from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_feedback():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Save feedback to a text file
    with open('feedback.txt', 'a') as f:
        f.write(f"Name: {name}\nEmail: {email}\nMessage: {message}\n---\n")

    return render_template('thankyou.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
