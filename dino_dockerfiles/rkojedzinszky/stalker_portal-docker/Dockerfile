FROM debian:jessie
MAINTAINER Richard Kojedzinszky <krichy@nmdps.net>

ENV STALKER_VERSION=master

RUN apt-get update && apt-get dist-upgrade -f -y && \
	apt-get install -y apache2 php5 php5-dev php5-mysql php-pear nodejs libapache2-mod-rpaf nodejs npm curl && \
	apt-get install -y --no-install-recommends cron mysql-client patch runit memcached locales && \
	rm -rf /etc/php5/cli && ln -sf apache2 /etc/php5/cli && \
	rm -f /etc/apache2/sites-enabled/* && \
	ln -sf /usr/share/i18n/SUPPORTED /etc/locale.gen && \
	locale-gen

ADD files/ /

RUN cd /var/www/html/ && mkdir stalker_portal && cd stalker_portal && \
	curl -L https://github.com/azhurb/stalker_portal/archive/${STALKER_VERSION}.tar.gz | tar xzf - --strip-components=1

RUN \
	pear channel-discover pear.phing.info && pear upgrade-all && \
	pear install --alldeps phing/phing

RUN \
	sed -i \
	-e '/^short_open_tag/s/.*/short_open_tag = On/' \
	-e '/user_agent=/s,.*,user_agent="Mozilla/5.0",g' \
	/etc/php5/apache2/php.ini && \
	a2dismod -f authz_user && \
	a2dismod -f autoindex && \
	a2dismod -f deflate && \
	a2dismod -f filter && \
	a2dismod -f negotiation && \
	a2dismod -f status && \
	a2enmod rewrite

RUN cd /var/www/html/stalker_portal/deploy/ && cp build.xml build.xml.orig && \
	patch -p0 < /build.xml.image.diff && rm /build.xml.image.diff && \
	phing && \
	rm -rf /var/cache/apt/* /var/lib/apt/lists/* && \
	mv build.xml.orig build.xml && patch -p0 < /build.xml.run.diff && \
	rm /build.xml.run.diff

WORKDIR /var/www/html

EXPOSE 80

ENTRYPOINT ["/entrypoint.sh"]

CMD ["runsvdir", "/etc/services"]
