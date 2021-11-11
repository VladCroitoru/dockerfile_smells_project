# syntax=docker/dockerfile:1
FROM ubuntu:20.04
RUN apt-get update
RUN apt-get install -y git python3 python3-pip

WORKDIR /www
RUN git clone https://github.com/CoderSherlock/investat.git

WORKDIR /www/investat
RUN pip3 install -r requirements.txt

WORKDIR /www/investat/investat
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
EXPOSE 8000
CMD ["python", "manage.py", "crontab", "add"]
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
