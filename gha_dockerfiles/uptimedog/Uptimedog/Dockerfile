FROM python:3.10

ENV PYTHONUNBUFFERED 1

RUN apt-get update

RUN pip install --upgrade pip

RUN mkdir /app

COPY requirements.txt /app/

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

RUN rm -rf ./assets

EXPOSE 8000

VOLUME /app/storage

CMD ["gunicorn"  , "-b", "0.0.0.0:8000", "app.wsgi"]
