FROM python:3.8.5-slim

COPY ./app app
COPY run.sh run.sh
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 8080
ENTRYPOINT /bin/sh run.sh

