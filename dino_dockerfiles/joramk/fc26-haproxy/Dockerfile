FROM    joramk/fc26-base
MAINTAINER joramk@gmail.com
ENV     container docker

LABEL   name="Fedora - HAproxy stable with Lets Encrypt" \
        vendor="https://github.com/joramk/fc26-haproxy" \
        license="none" \
        build-date="20180304" \
        maintainer="joramk" \
	issues="https://github.com/joramk/fc26-haproxy/issues"

RUN {	yum update -y; \
	yum install openssl haproxy certbot cronie procps-ng iputils socat yum-cron -y; \
        yum clean all && rm -rf /var/cache/yum; \
}

COPY    docker-entrypoint.sh /
COPY    scripts/certbot-* /usr/local/sbin/
COPY	haproxy.cron /etc/cron.daily/

RUN {	systemctl enable haproxy crond; \
	systemctl disable auditd; \
	touch /firstrun; \
	chmod +rx /docker-entrypoint.sh /etc/cron.daily/haproxy.cron; \
	chmod 700 /usr/local/sbin/certbot-*; \
	mkdir -p /etc/letsencrypt/live; \
}

HEALTHCHECK CMD systemctl -q is-active haproxy || exit 1
STOPSIGNAL SIGRTMIN+3
EXPOSE 80 443
VOLUME [ “/sys/fs/cgroup”, "/etc/haproxy", "/etc/letsencrypt" ]
ENTRYPOINT [ "/docker-entrypoint.sh" ]
CMD [ "/sbin/init" ]
