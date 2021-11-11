FROM x110dc/base
MAINTAINER Ludek Vesely <ludek.vesely@email.com>

RUN apt-get update && apt-get install -yq apache2-utils nginx && rm /etc/nginx/sites-enabled/default

EXPOSE 80

ENV USER foo
ENV PASSWORD bar
ENV SERVER_NAME quux
ENV UPSTREAM_ADDRESS 1.2.3.4
ENV UPSTREAM_PORT 80

ADD proxy.conf /etc/nginx/conf.d/
ADD run.sh /

CMD /run.sh
