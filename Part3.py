from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')

def Hello_World():
    return  render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    exp=request.form.get('exp')
    score=request.form.get('score')
    points=request.form.get('points')

    print(exp,score,points)

app.run(debug=True)