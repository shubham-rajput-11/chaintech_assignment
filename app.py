from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('index.html',time=current_time)






@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    
    submissions=[name,email]
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('submissions.html',submissions=submissions,time=current_time)






if __name__ == '__main__':
    app.run(debug=True)
