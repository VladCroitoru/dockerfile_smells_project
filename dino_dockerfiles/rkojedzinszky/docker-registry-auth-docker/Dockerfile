FROM alpine:3.14

MAINTAINER Richard Kojedzinszky <richard@kojedz.in>

ENV APP_USER=docker-registry-auth \
    APP_HOME=/opt/docker-registry-auth \
    AUTH_REVISION=6a7b9015d9ca3eb52e9a222bf12186d890c6960c

RUN apk add --no-cache python3 py3-pip openssl supervisor nginx py3-psycopg2 uwsgi-python3 openssl \
        py3-cryptography py3-jwt && \
	mkdir -p /data $APP_HOME && \
	adduser -u 17490 -D -H -h $APP_HOME $APP_USER && \
	chown -R $APP_USER /var/lib/nginx /var/log/nginx

RUN apk add --no-cache -t .build-deps curl tar && \
	cd /opt/docker-registry-auth && \
	curl -L https://github.com/rkojedzinszky/docker-registry-auth/archive/$AUTH_REVISION.tar.gz | tar xzf - --strip-components=1 && \
	pip3 install -r requirements.txt && \
	apk del .build-deps && \
	python3 manage.py collectstatic --no-input && \
	rm -rf /root/.cache && \
	ln -sf /data/local_settings.py

ADD assets/ /

EXPOSE 8080

WORKDIR $APP_HOME

ENV UWSGI_THREADS 4

USER 17490

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
