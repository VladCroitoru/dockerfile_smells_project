FROM python:3.8-slim-buster

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "run.py"]

ENV FLASK_ENV='docker'
