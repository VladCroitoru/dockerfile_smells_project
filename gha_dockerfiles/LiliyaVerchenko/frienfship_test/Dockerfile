FROM python:3.8

RUN mkdir /app
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN apt-get update -y \
 && pip install --upgrade pip \
 && pip install -r requirements.txt

CMD gunicorn -b 0.0.0.0:8000 --access-logfile - --error-logfile - friendship_project.wsgi
