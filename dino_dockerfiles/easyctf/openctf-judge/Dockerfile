FROM python:3.5.2

RUN apt-get update && apt-get install -y netcat

RUN mkdir /judge
COPY requirements.txt /judge/
WORKDIR /judge
RUN pip3 install -r requirements.txt
COPY . /judge/

CMD ["bash", "-c", "bash wait-for-db.sh && gunicorn --worker-class eventlet --bind 0.0.0.0:80 -w 1 main:app"]
