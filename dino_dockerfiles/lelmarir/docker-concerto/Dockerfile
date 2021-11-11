FROM ubuntu:16.04

MAINTAINER "Michele Preti" lelmarir@gmail.com

ADD ./scripts/install.sh /install.sh

RUN bash /install.sh

RUN apt-get clean
RUN apt-get update && apt-get install -y supervisor
RUN mkdir -p /var/log/supervisor
COPY ./config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

## Expose the MySQL and Apache port
EXPOSE 80 

CMD ["/usr/bin/supervisord"]