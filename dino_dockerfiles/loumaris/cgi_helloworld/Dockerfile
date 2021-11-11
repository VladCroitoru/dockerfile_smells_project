FROM nginx:latest
MAINTAINER Chrristian Heimke <chrisitan.heimke@loumaris.com>

RUN apt-get update && apt-get install -y fcgiwrap

COPY nginx.conf /etc/nginx/nginx.conf
COPY default.conf /etc/nginx/conf.d/default.conf

RUN mkdir /usr/lib/cgi-bin
COPY helloworld.cgi /usr/lib/cgi-bin/helloworld.cgi
RUN chmod a+x /usr/lib/cgi-bin/helloworld.cgi

COPY init.sh /init.sh

EXPOSE 80

ENTRYPOINT ["/init.sh"]
