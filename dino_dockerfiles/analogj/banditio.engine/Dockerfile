FROM smebberson/alpine-base

#install python & libraries
RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base \
	&& pip install virtualenv tornado\
	&& rm -rf /var/cache/apk/*

#install nginx
RUN apk add --update nginx git

#copy over the services
ADD services.d/ /etc/services.d/

#configure nginx
ADD nginx/nginx.conf /etc/nginx/nginx.conf
ADD nginx/engine.conf /etc/nginx/conf.d/engine.conf
RUN chown -R nginx:nginx /var/log/nginx && chmod -R 755 /var/log/nginx

WORKDIR /srv/banditio.engine

#clone the application code.
RUN git clone https://github.com/AnalogJ/banditio.engine.git .


EXPOSE 9000
EXPOSE 80
