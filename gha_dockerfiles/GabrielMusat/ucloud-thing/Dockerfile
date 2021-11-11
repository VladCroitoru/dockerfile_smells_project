FROM python:3.7

WORKDIR /app

COPY requirements.txt .

RUN apt update && apt install build-essential libdbus-glib-1-dev libgirepository1.0-dev python3-gi -y
RUN pip install vext pygobject
RUN pip install -r requirements.txt

COPY src .
COPY config.production.yml .

CMD python main.py