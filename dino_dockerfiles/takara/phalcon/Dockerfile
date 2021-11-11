FROM debian:8.7

MAINTAINER taka2063

WORKDIR /root/

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update
RUN apt-get -y install wget net-tools git make php5 apache2 \
	php5-dev php5-mysql vim curl chkconfig gcc libpcre3-dev 

# phalconインストール
RUN \
	git clone --depth=1 https://github.com/phalcon/cphalcon.git -b v3.4.1 && \
	cd /root/cphalcon/build && \
	./install && \
	rm -rf /root/cphalcon

# phalcon設定
COPY asset/phalcon.ini /etc/php5/mods-available/
RUN ln -s /etc/php5/mods-available/phalcon.ini /etc/php5/apache2/conf.d/20-phalcon.ini
RUN ln -s /etc/php5/mods-available/phalcon.ini /etc/php5/cli/conf.d/20-phalcon.ini

# composer
RUN curl -s http://getcomposer.org/installer | php
RUN chmod +x composer.phar
RUN mv composer.phar /usr/local/bin/composer

# box
WORKDIR /root/
RUN curl -LSs https://box-project.github.io/box2/installer.php | php
RUN mv box.phar /usr/local/bin/box

# phalcon devtools
COPY asset/box.json /root/
RUN \
	git clone https://github.com/phalcon/phalcon-devtools.git -b v3.4.0 && \
	cd /root/phalcon-devtools && \
	mv /root/box.json . && \
	composer install && \
	echo "phar.readonly = Off" >> /etc/php5/cli/php.ini && \
	box build && \
	mv phalcon.phar /usr/local/bin/phalcon && \
	chmod +x /usr/local/bin/phalcon && \
	cd /root && rm -rf phalcon-devtools

# phpunit
#RUN wget https://phar.phpunit.de/phpunit-4.8.19.phar -O /usr/local/bin/phpunit && \
#	chmod +x /usr/local/bin/phpunit

# 設定ファイルコピー
COPY asset/apache2.conf /etc/apache2/
COPY asset/default /etc/apache2/sites-available/
COPY asset/php.ini /etc/php5/apache2/
RUN a2enmod rewrite
RUN mkdir -p /var/log/phalcon && chown www-data.www-data /var/log/phalcon
ENV DEBIAN_FRONTEND dialog
#
# tty停止
COPY asset/ttystop /etc/init.d/
RUN chkconfig --add ttystop

EXPOSE 80

WORKDIR /var/www/

CMD ["/sbin/init", "3"]
