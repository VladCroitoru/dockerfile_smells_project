FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /website

WORKDIR /website
ADD requirements.txt /website/
RUN pip install -r requirements.txt
ADD . /website/