FROM python:3.8-slim-buster

COPY . /app

WORKDIR /app

RUN pip install flask
RUN pip install -r requirements.txt

ENTRYPOINT ["gunicorn", "-b", ":8080", "main:APP"]
