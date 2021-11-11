FROM python:3.9.5

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./mysite .

CMD gunicorn mysite.wsgi:application --bind 0.0.0.0:8000