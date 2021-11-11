FROM python:3-alpine

RUN apk --no-cache add parallel
RUN pip --no-cache-dir install plotly==2.0.0
COPY plotly.offline.example.py /
