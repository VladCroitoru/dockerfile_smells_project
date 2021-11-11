FROM node:latest
MAINTAINER Tiago Pires <tandrepires@gmail.com>

ENV YOD_HOME /yod-setup
ENV HOME $YOD_HOME

ADD Dockerfile-setup $YOD_HOME/Dockerfile
ADD setup.sh $YOD_HOME/setup.sh
ADD scripts/* $YOD_HOME/scripts/

RUN apt-get clean && rm -rf /var/lib/apt/lists/* && \
    npm install -g yo

# download latest docker client
RUN curl https://get.docker.io/builds/Linux/x86_64/docker-1.4.1 -o /usr/local/bin/docker && \
    chmod +x /usr/local/bin/docker $YOD_HOME/setup.sh $YOD_HOME/scripts/*

WORKDIR $YOD_HOME
CMD ["/bin/bash","-c","setup.sh"]
