# syntax=docker/dockerfile:1
FROM python:3.7-alpine
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
ENV FLASK_APP=./notification_service/app.py
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]