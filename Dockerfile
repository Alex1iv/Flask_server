FROM tiangolo/uwsgi-nginx-flask:python3.10

#WORKDIR usr/src/app

COPY ./app/ ./
COPY ./requirements.txt ./
COPY ./uwsgi.ini ./

RUN pip install --no-cache-dir -r requirements.txt

#CMD ["python", "./server.py"] 