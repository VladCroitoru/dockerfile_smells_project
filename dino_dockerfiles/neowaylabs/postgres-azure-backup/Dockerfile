FROM ubuntu:latest

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y -q && \
  apt-get install -y nodejs-legacy curl wget npm && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

RUN npm install -g n azure-cli
RUN n 0.12.7

RUN wget -q https://www.postgresql.org/media/keys/ACCC4CF8.asc -O - | apt-key add -
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main" >> /etc/apt/sources.list.d/pgdg.list

RUN apt-get update -y && \
    apt-get install -y postgresql

RUN azure telemetry --disable

ADD start.sh /start.sh
RUN chmod 0755 /start.sh

ENTRYPOINT ["/start.sh"]