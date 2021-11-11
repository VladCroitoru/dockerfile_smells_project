FROM    joramk/el7-base
MAINTAINER joramk@gmail.com
ENV     container docker

LABEL   name="CentOS 7 - Latest Apache / PHP stable / phpMyAdmin" \
        vendor="https://github.com/joramk/el7-httpd-php" \
        license="none" \
        build-date="20171008" \
        maintainer="joramk@gmail.com"

RUN {   yum install http://rpms.famillecollet.com/enterprise/remi-release-7.rpm -y; \
	yum-config-manager --enable remi-php71 --enable remi; \
        yum install httpd openssl logrotate \
	php php-json php-cli php-pecl-http \
        php-mbstring php-mysqlnd php-gd php-xml \
        php-bcmath runtime php-common php-pdo \
        php-process php-tidy php-soap -y; \
        yum clean all; rm -rf /var/cache/yum; \
}

COPY    ./docker-entrypoint.sh /
RUN {   systemctl enable httpd crond; \
        touch /firstrun; \
        chmod +rx /docker-entrypoint.sh; \
}

HEALTHCHECK CMD systemctl -q is-active httpd || exit 1

VOLUME  [ "/sys/fs/cgroup" ]

EXPOSE  80
STOPSIGNAL SIGRTMIN+3
ENTRYPOINT [ "/docker-entrypoint.sh" ]
CMD [ "/sbin/init" ]
