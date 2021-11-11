FROM openjdk:8-jre

MAINTAINER Marc Navarro https://github.com/morfeo8marc

# update packages and install basics
RUN  \
  export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
     apt-get -y upgrade && \
     apt-get install -y vim wget curl git

# create working directory
RUN mkdir -p /redis-stat

RUN wget https://github.com/junegunn/redis-stat/releases/download/0.4.11/redis-stat-0.4.11.jar  -P /redis-stat

WORKDIR /redis-stat

EXPOSE 63790

ADD run.sh /redis-stat/

RUN chmod 744 /redis-stat/run.sh

CMD /redis-stat/run.sh
