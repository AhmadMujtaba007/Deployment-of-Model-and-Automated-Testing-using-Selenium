from flask import Flask , render_template , request
import  numpy as np
import pickle

model = pickle.load(open('LR_Model.pkl', 'rb'))
app = Flask(__name__)
@app.route('/' , methods = [  'GET' , 'POST'])
def predict():
    if request.method == 'POST':
        First_Entry = request.form.get('fnum')
        Second_Entry = request.form.get('lnum')
        X = np.hstack((First_Entry,Second_Entry ))
        X = np.reshape(X, (-1, 2))
        y_pred = model.predict(X)
        print(X)
        print(y_pred)
        # return render_template("home.html")
        return render_template("home.html" , prediction = y_pred )
    else:
        return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True, port=5000, use_reloader=False)