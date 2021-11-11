FROM ubuntu:16.04
LABEL maintainer="Sean Cheung <theoxuanx@gmail.com>"

ARG CN_MIRROR=false
RUN if [ "$CN_MIRROR" = true ]; then sed -i 's#http://\(archive\|security\).ubuntu.com/#http://mirrors.aliyun.com/#' /etc/apt/sources.list; fi

RUN set -ex \
    && apt-get update \
    && export DEBIAN_FRONTEND="noninteractive" \
    && echo "Install Dependencies..." \
    && apt-get update \
    && apt-get install -y --no-install-recommends curl ca-certificates \
        mysql-server mysql-client bash openssl supervisor apache2 \
        php libapache2-mod-php php-mcrypt php-mysql \
        php-curl php-gd php-mbstring php-xml php-xmlrpc\
	&& echo "Initializing directories..." \
    && for path in \
		/var/run/mysqld \
		/var/log/mysql \
		/var/opt/mysql \
	; do \
	mkdir -p "$path"; \
    chown mysql:mysql "$path"; \
	done \
    && sed -ri "s/^(\s*)(DocumentRoot.+)$/\1\2\n\1DirectoryIndex index.php index.html/" /etc/apache2/sites-available/000-default.conf \
    && sed -ri "s/^(\s*)#(ServerName\s*).+$/\1\2localhost/" /etc/apache2/sites-available/000-default.conf \
    && sed -i "s/Indexes\s*//g" /etc/apache2/apache2.conf \
    && echo "Clean Up..." \
    && rm /var/www/html/* \
    && rm -rf /var/lib/apt/lists/*

COPY supervisord.conf /etc/supervisor/
COPY entrypoint.sh /entrypoint.sh

VOLUME ["/var/opt/mysql"]
EXPOSE 3306 80

ENTRYPOINT ["/entrypoint.sh"]
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]