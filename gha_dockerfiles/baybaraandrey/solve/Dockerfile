FROM python:3.8.3-slim-buster

RUN mkdir /app
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["sh", "entrypoint.sh"]
