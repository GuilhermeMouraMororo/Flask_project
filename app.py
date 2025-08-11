from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def run():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def marks():
    number=int(request.form['Number'])
    result = number ** 2
    return render_template('home.html',Percentage=result)

if __name__=='__main__':
    app.run(debug=True)



