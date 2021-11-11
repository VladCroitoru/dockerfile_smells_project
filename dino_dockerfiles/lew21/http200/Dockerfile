FROM python:3.6

RUN mkdir /app
WORKDIR /app
ENV PYTHONPATH /app

ADD requirements.txt /app/
RUN pip install -r requirements.txt

ADD app.py /app/

CMD ["gunicorn", "-b", "[::]:80", "app"]
