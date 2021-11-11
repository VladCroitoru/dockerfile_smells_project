FROM python:2.7-alpine

MAINTAINER lyremelody@163.com

ADD requirements.txt *.py /

RUN pip install -r /requirements.txt

WORKDIR /

CMD python cli.py
