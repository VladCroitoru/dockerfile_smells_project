FROM debian:wheezy

RUN \
	echo deb http://http.debian.net/debian wheezy-backports main >> /etc/apt/sources.list \
	&& echo 'APT::Install-Recommends "0";' > /etc/apt/apt.conf.d/99norecommends \
	&& sed -i 's/deb/deb [arch=amd64]/' /etc/apt/sources.list \
	&& apt-get update \
	&& apt-get -t wheezy-backports -f -y dist-upgrade \
	&& apt-get -t wheezy-backports -f -y upgrade \
	&& apt-get -t wheezy-backports install -y nginx-extras \
	&& apt-get clean \
	&& rm /var/lib/apt/lists/*.* \
	&& sed -i '1i\daemon off;' /etc/nginx/nginx.conf \
	&& sed -i 's|#.*server_tokens off|server_tokens off|' /etc/nginx/nginx.conf \
	&& sed -i 's|access_log /var/log/nginx/access.log|access_log off|' /etc/nginx/nginx.conf \
	&& sed -i 's|error_log /var/log/nginx/error.log|error_log /dev/null|' /etc/nginx/nginx.conf

EXPOSE 80
CMD ["nginx"]
