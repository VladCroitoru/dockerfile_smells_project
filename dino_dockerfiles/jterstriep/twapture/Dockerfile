FROM python:2.7
MAINTAINER Jeff Terstriep <jefft@illinois.edu>

RUN mkdir -p /app/data /app/logs
VOLUME /app/data /app/logs 

COPY . /app
WORKDIR /app
RUN python setup.py install

CMD ["twapture", "--help"]
