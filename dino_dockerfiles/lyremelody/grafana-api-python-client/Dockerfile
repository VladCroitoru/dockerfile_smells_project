FROM python:3.6.3-alpine

MAINTAINER lyremelody@163.com

ADD requirements.txt *.py gapi_client /

RUN pip install -r /requirements.txt

WORKDIR /

CMD python gcli.py
