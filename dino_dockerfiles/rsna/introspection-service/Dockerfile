FROM python:3
MAINTAINER Josh Mandel

# Install required packages
RUN apt-get update
RUN apt-get install -y \
    supervisor
RUN apt-get clean

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 5000

# Set the environment
ENV FLASK_APP /usr/src/app/app.py
ENV API_SERVER https://portal-stu3.demo.syncfor.science/api/fhir
ENV API_SERVER_NAME 'SMART STU-3 PORTAL'

CMD ["supervisord", "-c", "supervisord.conf"]
