FROM ubuntu:14.04

RUN apt-get update
RUN apt-get install -y wget make gcc binutils python-pip python-dev libssl-dev libffi-dev bash

WORKDIR /root

RUN wget http://www.haproxy.org/download/1.5/src/haproxy-1.5.1.tar.gz
RUN tar -zxvf haproxy-1.5.1.tar.gz

RUN cd haproxy-1.5.1 && make TARGET=generic && make install

ADD . /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN touch /var/run/haproxy.pid

EXPOSE 1936

CMD ["python", "-m", "discovery"]

