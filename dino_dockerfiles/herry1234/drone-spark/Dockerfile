# Docker image for a Drone notification plugin for Cisco Spark

FROM python:alpine
MAINTAINER Hank Preston <hank.preston@gmail.com>

RUN mkdir -p /usr/src/drone-spark
WORKDIR /usr/src/drone-spark

COPY requirements.txt /usr/src/drone-spark/
RUN pip install -r requirements.txt

COPY send_message.py /usr/src/drone-spark/

ENTRYPOINT ["python", "send_message.py"]
