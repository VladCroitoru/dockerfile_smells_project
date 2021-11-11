FROM ubuntu:14.04
RUN apt-get update
RUN apt-get install -y python-pip
RUN pip install shadowsocks 

COPY ./ServerStart.sh ./ServerStart.sh 

ENTRYPOINT ["/bin/sh","./ServerStart.sh"]

