FROM python:3.8.2

ADD . /flask-deploy

WORKDIR /flask-deploy

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install gunicorn[gevent]

EXPOSE 5000

CMD gunicorn --worker-class gevent --workers 8 --bind 0.0.0.0:5000 app:app --log-level info