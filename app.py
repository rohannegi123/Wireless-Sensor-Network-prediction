from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import pickle
from PIL import Image


app = Flask(__name__)

@app.route('/' , methods =['GET'])
@cross_origin()
def homepage():

    img_PIL = Image.open('secsor.jpg')
    return render_template('index.html' , img = img_PIL )

@app.route('/predict', methods =['POST' , 'GET'])
@cross_origin()
def Prediction():
    if request.method == 'POST':
        try:
            avg_rss12 = float(request.form['avg_rss12'])
            var_rss12 = float(request.form['var_rss12'])
            avg_rss13 = float(request.form['avg_rss13'])
            var_rss13 = float(request.form['var_rss13'])
            avg_rss23 = float(request.form['avg_rss23'])
            var_rss23 = float(request.form['var_rss23'])


            filename = 'senord_newtocg.pickle'
            load_model = pickle.load(open(filename, 'rb'))
            predictionans = load_model.predict([[avg_rss12, var_rss12, avg_rss13, var_rss13, avg_rss23, var_rss23]])
            if predictionans == 1:
                prediction = 'Bending one'
                image = 'https://blogger.googleusercontent.com/img/a/AVvXsEjuhH4CsQhgbaZRd-c4lltwUuLm1iU5Nz2jUELvM57DFSvAqmlcK2rmW3uNRKV_hFWJL7HS79zwgK61IWJRbBqxoSn4L-up-xUf9sWg8k1fRktmDnWImBaS5AfyeJ5Q9XDhg8V_5hAJQU7wP4YmfZEwoG78TKZ0awKeplGcrSCDJ5fhij0EXiq7qbDo=w373-h478'
            elif predictionans == 2:
                prediction = 'Bending two'
                image = 'https://blogger.googleusercontent.com/img/a/AVvXsEgEKwy3153n5x6QJrURZz3fvw8_Phw50N7c7-xUdHdyyJKu7stoY2qUMYnT97A1k7m2sdPagAsquxLCgq3u6M1SirlqHASPYHSGI7k2aRWrVdwcv0Uj2bdMXXpmNzpDo0bbY88QRzFSSqMALr4uWNo1uOuiemuEG6i94HtikqQnA8egQTbpB-nuEIE2=w366-h468'
            elif predictionans == 3:
                image = 'https://bali.hardrockhotels.net/wp-content/uploads/2020/07/cycling-as-new-normal.jpg'
                prediction = 'Cycling'
            elif predictionans == 4:
                prediction = 'Lying'
                image = 'https://image.shutterstock.com/image-vector/teen-boy-lying-on-flat-260nw-408687199.jpg'
            elif predictionans == 5:
                prediction = 'Standing'
                image = 'https://emojipedia-us.s3.amazonaws.com/source/skype/289/man-standing_1f9cd-200d-2642-fe0f.png'
            else :
                prediction = 'Walking'
                image =  'data:image/png;base64,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'

            return render_template('results.html' , prediction = prediction , image = image)

        except Exception as e:
            print('the exception msg is : ', e)
            return 'Something went wrong'
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug = True)