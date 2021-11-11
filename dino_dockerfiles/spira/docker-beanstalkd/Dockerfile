FROM spira/docker-base

MAINTAINER "Zak Henry" <zak.henry@gmail.com>

RUN apt-get update -y && \
    apt-get install -y aptitude && \
    aptitude install -y beanstalkd

EXPOSE 11300

ENTRYPOINT ["beanstalkd","-p","11300"]