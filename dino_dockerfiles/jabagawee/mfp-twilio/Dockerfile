FROM python:alpine

RUN pip install flask

COPY . /app
WORKDIR /app

EXPOSE 5000

ENV FLASK_APP=main.py
CMD ["flask", "run", "--host", "0.0.0.0"]
