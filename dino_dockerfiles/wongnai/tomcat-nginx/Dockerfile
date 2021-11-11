FROM tomcat:8.5.20-jre8

MAINTAINER Suparit Krityakien <suparit@wongnai.com>

##### The nginx setup is basically copied from https://hub.docker.com/_/nginx/ (alpine)
ENV NGINX_VERSION 1.12.1-1~stretch

RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \
	&& echo "deb http://nginx.org/packages/debian/ stretch nginx" >> /etc/apt/sources.list \
	&& apt-get update \
	&& apt-get install --no-install-recommends --no-install-suggests -y \
		ca-certificates \
		nginx=${NGINX_VERSION} \
		nginx-module-xslt \
		nginx-module-geoip \
		nginx-module-image-filter \
		nginx-module-perl \
		nginx-module-njs \
		gettext-base \
		vim \
		openjdk-8-jdk \
		ca-certificates-java \
	&& rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log \
	&& ln -sf /dev/stdout /usr/local/tomcat/logs/catalina.out
	 
ENV WARMUP 1
ENV START_NGINX 1

COPY tomcat/ /usr/local/tomcat/

WORKDIR /usr/local/tomcat

RUN chmod +x /usr/local/tomcat/bin/docker-entrypoint.sh

EXPOSE 80 443 8080 8000

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["start"]
