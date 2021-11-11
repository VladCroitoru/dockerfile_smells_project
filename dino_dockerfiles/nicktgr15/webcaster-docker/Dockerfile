FROM ubuntu:16.04 

RUN apt-get update -y 
RUN apt-get install git vim python make -y

RUN git clone https://github.com/nicktgr15/webcaster.git 

RUN openssl req -new -x509 -keyout /tmp/server.pem -out /tmp/server.pem -days 365 -nodes -subj "/C=GB/L=London/O=MyCompany/OU=MyOU/CN=MyCN"

COPY run.py /webcaster/https/run.py

WORKDIR /webcaster

ENTRYPOINT make run
