FROM nginx:1.16.0

ADD package.zip.enc /home

RUN apt-get update -y && \
	apt-get install unzip openssl -y && \
	apt-get clean

CMD cd /home && \	
	openssl enc -d -aes-256-cbc -in package.zip.enc -out package.zip -pass pass:$UNLOCK_KEY -md md5 && \
	unzip package.zip && \
	mkdir -p /etc/nginx && \
	mkdir -p /var/tmp/nginx && \
	mv package/* /etc/nginx && \	
	nginx -g 'daemon off;' -c /etc/nginx/nginx.conf