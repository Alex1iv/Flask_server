# request обрабaтывает запросы. Jonify - возвращает в  формате JSON
from datetime import datetime
from flask import Flask, request, jsonify 
import numpy as np
import pickle

with open("models/model.pkl", "rb") as pkl_file:
    model = pickle.load(pkl_file)

# создаём приложение и одноименный процесс Python
app = Flask(__name__) 

# эндпоинт обработки поступающих POST-запросов
@app.route('/predict', methods=['POST'])
def predict():
    features = np.array(request.json).reshape(1, 8)
    prediction = model.predict(features)[0]
    return jsonify({'prediction': prediction})

# эндпоинт проверки работы сервера
# соответствует обращению к сайту по дефолтному адресу: http://localhost:5000/.
@app.route('/') 
def index():
    msg = "Test message. The server is running now: "
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return msg + str(time)

if __name__ == '__main__':
    #app.run('localhost', 5000)
    """
    когда мы запускаем веб-сервис в контейнере, для тестирования сервера необходимо пользоваться широковещательным адресом (0.0.0.0) — это позволит вам обеспечить доступ к вашему контейнеру
    """
    app.run(host='0.0.0.0', port=5000)
    
    
