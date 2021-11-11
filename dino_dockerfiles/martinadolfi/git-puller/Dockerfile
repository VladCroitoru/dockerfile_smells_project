FROM debian:jessie

MAINTAINER Martin Gonzalez Adolfi <martinadolfi@gmail.com>

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*
RUN echo StrictHostKeyChecking no >> /etc/ssh/ssh_config
ADD startup.sh /usr/bin/startup.sh
RUN chmod a+x /usr/bin/startup.sh
WORKDIR /src/
VOLUME /src
CMD startup.sh
