FROM alpine:3.2
MAINTAINER admin@tropicloud.net

ADD . /app
WORKDIR /app
RUN apk add curl unzip \
	php-cli \
	php-common \
	php-mysqli \
	php-pdo_mysql \
	php-pdo_pgsql \
	php-pdo_sqlite \
	--update && \
	curl -sL http://www.adminer.org/latest-en.php > index.php && \
	curl -sL https://github.com/interconnectit/Search-Replace-DB/archive/master.zip > master.zip && \
	unzip master.zip && rm -f master.zip

EXPOSE 80
CMD /app/start.sh
