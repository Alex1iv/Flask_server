import requests
import numpy as np
from numpy.random import randint
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
# загружаем данные
X, y = fetch_california_housing(return_X_y=True) 

idx = randint(X.shape[0], size=3)
X_test, y_test = X[idx,:], y[idx]

if __name__ == '__main__':
    # выполняем POST-запрос на сервер по эндпоинту add с параметром json
    for i in range(X_test.shape[0]):
        
        r = requests.post('http://localhost:80/predict', json=X_test[i,:].tolist()) 
        
        
        # выводим статус запроса
        #print('Status code: {}'.format(r.status_code))
        
        # реализуем обработку результата
        if r.status_code == 200:
            # если запрос выполнен успешно (код обработки=200),выводим результат на экран
            print(r.json()['prediction'])
        else:
            # если запрос завершён с кодом, отличным от 200, выводим содержимое ответа
            print(r.text)