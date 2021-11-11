FROM vladus2000/arch-base-yay
MAINTAINER vladus2000 <docker@matt.land>

COPY shiz/ /home/evil/shiz/

RUN \
	/install-devel.sh && \
	mkdir -p /config/{rtorrent,rutorrent} /downloads && \
	chown evil:evil -R /config /downloads && \
	ln -s /config/rtorrent /home/evil/rtorrent && \
	su - evil -c 'yay -S --needed --noconfirm rsync rtorrent geoip php-geoip plowshare mktorrent nginx irssi perl-archive-zip perl-digest-sha1 perl-html-parser perl-json perl-json-xs perl-net-ssleay perl-xml-libxml perl-xml-libxslt fcgi fcgiwrap spawn-fcgi screen php-fpm mediainfo procps-ng python-cfscrape nodejs python-requests-toolbelt python-setuptools' && \
	pacman -S --needed --noconfirm python-pip python-asn1crypto python-brotli python-cffi python-cryptography python-pycparser python-pyopenssl python-tzlocal && \
	pip install cloudscraper && \
	chown -R evil ~evil/shiz && \
	su - evil -c 'mkdir -p ~/.irssi/scripts/autorun && cd ~/.irssi/scripts && git init && git remote add origin https://github.com/autodl-community/autodl-irssi.git && git pull origin master && cp autodl-irssi.pl autorun/ && mkdir -p ~/.autodl && cp ~/shiz/autodl.cfg /config && ln -s /config/autodl.cfg ~/.autodl/autodl.cfg && cp ~/shiz/.rtorrent.rc /config/.rtorrent.rc && ln -s /config/.rtorrent.rc ~/.rtorrent.rc && mkdir -p ~/rtorrent/.session && ln -s /downloads ~/downloads' && \
	mkdir -p /usr/share/webapps && \
	cd /usr/share/webapps && \
	git clone https://github.com/Novik/ruTorrent.git && \
	mv ruTorrent rutorrent && \
	cd /usr/share/webapps/rutorrent/plugins && \
	git clone https://github.com/autodl-community/autodl-rutorrent.git autodl-irssi && \
	cp autodl-irssi/_conf.php autodl-irssi/conf.php && \
	cd /usr/share/webapps/ && \
	chown http:http -R rutorrent && \
	cp ~evil/shiz/conf.php /usr/share/webapps/rutorrent/plugins/autodl-irssi/ && \
	cp ~evil/shiz/config.php /usr/share/webapps/rutorrent/conf/ && \
	cp ~evil/shiz/run_rtorrent.sh / && \
	cp ~evil/shiz/base_startup.sh / && \
	cp ~evil/shiz/startup.sh / && \
	cp ~evil/shiz/nginx.conf /etc/nginx/ && \
	chmod +x /startup.sh /base_startup.sh && \
	chown -R evil:evil /usr/share/webapps/rutorrent && \
	sed -e 's/;extension=sockets/extension=sockets/' /etc/php/php.ini > /php.ini && \
	mv /php.ini /etc/php/php.ini && \
	rm -rf /usr/share/webapps/rutorrent/share/settings && \
	ln -s /config/rutorrent /usr/share/webapps/rutorrent/share/settings && \
	echo net.core.rmem_max = 16777216 >> /etc/sysctl.d/99-sysctl.conf && \
	echo net.core.wmem_max = 16777216 >> /etc/sysctl.d/99-sysctl.conf && \
	echo net.ipv4.tcp_wmem = 4096 12582912 16777216 >> /etc/sysctl.d/99-sysctl.conf && \
	echo net.ipv4.tcp_rmem = 4096 12582912 16777216 >> /etc/sysctl.d/99-sysctl.conf && \
	echo net.ipv4.tcp_slow_start_after_idle = 0 >> /etc/sysctl.d/99-sysctl.conf && \
	echo net.core.netdev_max_backlog = 5000 >> /etc/sysctl.d/99-sysctl.conf && \
	echo net.core.optmem_max = 65536 >> /etc/sysctl.d/99-sysctl.conf && \
	echo net.core.rmem_default = 1048576 >> /etc/sysctl.d/99-sysctl.conf && \
	echo net.core.wmem_default = 1048576 >> /etc/sysctl.d/99-sysctl.conf && \
	echo net.ipv4.tcp_fastopen = 3 >> /etc/sysctl.d/99-sysctl.conf && \
	/rm-devel.sh

EXPOSE 8069
EXPOSE 49152

CMD /bin/bash -c /startup.sh

VOLUME /config
VOLUME /downloads

