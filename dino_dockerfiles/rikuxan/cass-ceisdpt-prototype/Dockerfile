FROM python:3.6.2
MAINTAINER Philipp Holler <philipp.holler93@gmail.com>

RUN pip install scipy pyinterval ujson
ADD cass-ceisdpt-prototype.py problem-data.json /opt/
WORKDIR /opt

ENTRYPOINT ["python3", "/opt/cass-ceisdpt-prototype.py"]
