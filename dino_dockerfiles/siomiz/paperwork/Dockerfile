FROM gliderlabs/alpine:3.2

MAINTAINER Tomohisa Kusano <siomiz@gmail.com>

WORKDIR /opt/paperwork

RUN apk --update add \
	curl \
	git \
	lighttpd \
	nodejs \
	php \
	php-cgi \
	php-ctype \
	php-curl \
	php-dom \
	php-gd \
	php-iconv \
	php-json \
	php-mcrypt \
	php-openssl \
	php-pdo \
	php-pdo_mysql \
	php-phar

RUN git clone --depth 1 https://github.com/twostairs/paperwork.git .

COPY strict.patch /opt/paperwork/
RUN patch -p1 < strict.patch && rm strict.patch

RUN curl -sSL https://getcomposer.org/installer | php

WORKDIR /opt/paperwork/frontend

RUN ../composer.phar install --prefer-source --no-interaction

RUN npm install -g gulp bower \
	&& npm install \
	&& bower --allow-root install \
	&& gulp \
	&& chown -R lighttpd.lighttpd app/storage \
	&& sed -ir '/registration/s/true/false/' app/config/paperwork.php \
	&& sed -ir '/showIssueReportingLink/s/true/false/' app/config/paperwork.php \
	&& echo 'mysql, mysql, 3306, paperwork, paperwork' > app/storage/db_settings

COPY lighttpd.conf /etc/lighttpd/

VOLUME ["/opt/paperwork/frontend/app/storage/"]

CMD ["lighttpd", "-f", "/etc/lighttpd/lighttpd.conf", "-D"]

EXPOSE 80

