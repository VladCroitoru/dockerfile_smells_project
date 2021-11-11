FROM ubuntu:latest

COPY ./src /app
COPY requirements.txt /
COPY config.json /

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

RUN apt-get update && \
    apt-get install ffmpeg python3-pip python3 -y && \
    pip3 install -r requirements.txt

WORKDIR /app
ENTRYPOINT ["python3", "api.py"]