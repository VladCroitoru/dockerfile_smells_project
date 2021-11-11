FROM ubuntu:14.04

RUN apt-get update -y
RUN apt-get install -y python python-pip curl
RUN pip install doit doit-py doit-cmd ipython
RUN curl -sSL https://get.docker.com/ubuntu/ | sudo sh
COPY usage.sh /usage.sh
COPY alias.sh /alias
COPY extra/ /extra

ENV DOCKER_HOST=unix:///docker.sock
ENV PYTHONPATH=/extra

VOLUME /target
WORKDIR /target

CMD ["/usage.sh"]
