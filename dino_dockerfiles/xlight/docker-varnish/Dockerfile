FROM debian:jessie

RUN apt-get update
RUN apt-get install -y apt-transport-https curl
RUN curl https://repo.varnish-cache.org/GPG-key.txt | apt-key add -
RUN echo "deb https://repo.varnish-cache.org/debian/ jessie varnish-4.1" >> /etc/apt/sources.list.d/varnish-cache.list
RUN apt-get update
RUN apt-get install -y varnish
RUN apt-get clean
RUN curl https://raw.githubusercontent.com/xlight/varnish-4.0-configuration-templates/master/default.vcl -o /etc/varnish/default.vcl
WORKDIR /root
ENV BACKEND_PORT 80
ENV CACHE_SIZE 256m
ENV SERV_PORT 6081
RUN curl https://raw.githubusercontent.com/xlight/Docker-varnish/master/start.sh -o/root/start.sh
CMD sh /root/start.sh
