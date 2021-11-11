# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /

COPY setup.py .
COPY simpleSIR/ ./simpleSIR/

RUN pip install -e .

CMD [ "python3", "-m" , "simpleSIR"]