# A Dockerfile specifies how to build a Docker image
FROM python:3.7

ADD flask_learning/ /app
WORKDIR /app

RUN python3 -m venv env
RUN pip install --upgrade pip

RUN pip install Flask
RUN pip install Werkzeug
RUN pip install pymongo
RUN pip install flask_sqlalchemy
RUN pip install flask_mail

# CMD gunicorn app:app -w 2 --threads 2 -b 0.0.0.0:8080
ENTRYPOINT ["python", "app.py"]