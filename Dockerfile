FROM tiangolo/uwsgi-nginx-flask:python3.8

RUN pip install --no-cache flask-mysql==1.5.1 && mkdir /logs

COPY ./app /app
