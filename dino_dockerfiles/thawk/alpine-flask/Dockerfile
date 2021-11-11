FROM alpine
MAINTAINER thawk <thawk009@gmail.com>

# basic flask environment
RUN apk add --no-cache bash git nginx uwsgi uwsgi-python py2-pip dropbear-ssh \
	&& pip2 install --upgrade pip \
	&& pip2 install flask

# application folder
ENV APP_DIR /app

# app dir
RUN mkdir /app \
	&& chown -R nginx:nginx /app \
	&& chmod 777 /run/ -R \
	&& chmod 777 /root/ -R

VOLUME ${APP_DIR}
WORKDIR ${APP_DIR}

# expose web server port
# only http, for ssl use reverse proxy
EXPOSE 80

# copy config files into filesystem
COPY nginx.conf /etc/nginx/nginx.conf
COPY app.ini /app.ini
COPY entrypoint.sh /entrypoint.sh

# exectute start up script
ENTRYPOINT ["/entrypoint.sh"]
