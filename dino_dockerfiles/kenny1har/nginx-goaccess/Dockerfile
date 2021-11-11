FROM ubuntu:16.04

MAINTAINER Kenny Hartono <https://kenny.id>

RUN apt-get update
RUN apt-get install -y wget curl
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash
RUN echo "deb http://deb.goaccess.io/ trusty main" | tee -a /etc/apt/sources.list.d/goaccess.list
RUN wget -O - http://deb.goaccess.io/gnugpg.key | apt-key add -
RUN apt-get update
RUN apt-get install -y goaccess nodejs multitail
RUN npm install http-server-with-auth -g
RUN apt-get autoremove -y && apt-get clean
RUN mkdir /var/log/nginx
RUN mkdir /app
RUN touch /var/log/nginx/access.sample.log
ADD goaccess.conf /etc/goaccess.conf
ADD run.sh /run.sh
EXPOSE 80
EXPOSE 8081
CMD ["/bin/bash", "/run.sh"]
