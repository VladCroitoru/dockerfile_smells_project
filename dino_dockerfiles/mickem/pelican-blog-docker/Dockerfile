FROM ubuntu:trusty
MAINTAINER Michael Medin <michael@medin.name>

RUN apt-get update && \
	apt-get install -y nginx && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/*

RUN apt-get update -y && \
	apt-get install --no-install-recommends -y -q curl build-essential ca-certificates git libjpeg-dev zlib1g-dev python-dev python-pip python-pelican

ONBUILD ADD . /site-source
ONBUILD RUN cd /site-source && \
	python make.py setup && \
	python make.py publish

ONBUILD RUN cp -R /site-source/output /app/

RUN rm /etc/nginx/sites-enabled/default
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
ADD sites-enabled/ /etc/nginx/sites-enabled/

EXPOSE 80

CMD ["/usr/sbin/nginx"]