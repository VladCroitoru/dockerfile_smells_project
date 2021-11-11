FROM debian:jessie

RUN apt-get update &&\
 apt-get upgrade -y &&\
 apt-get install -y fio &&\
 rm -rf /var/lib/apt/lists/*
 
ADD ./fio/ /fio/
ADD ./test.sh /test.sh
RUN chmod +x /test.sh

ENTRYPOINT ["/test.sh"]