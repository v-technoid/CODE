from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
@app.route('/register')
#def home():
 #   return "Home Page"
def homepage():
    return render_template('register.html')
    
@app.route("/confirm", methods=['POST', 'GET'])

def register():
    if request.method == 'POST':
        n = request.form.get('name')
        b = request.form.get('age')
        c = request.form.get('city')
        return render_template('confirm.html', name= n,age= b,city= c)

if __name__ == "__main__":
    app.run(debug=True)