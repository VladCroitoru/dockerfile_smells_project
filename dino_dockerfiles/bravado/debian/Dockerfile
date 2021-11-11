FROM debian:stretch-slim

# Set term and locale
ENV TERM=xterm \
LANG=C.UTF-8 \
LANGUAGE=C.UTF-8 \
LC_ALL=C.UTF-8

RUN echo 'path-include /usr/share/locale/pt*' >> /etc/dpkg/dpkg.cfg.d/docker \
	&& echo 'path-include /usr/share/locale/en*' >> /etc/dpkg/dpkg.cfg.d/docker

RUN export DEBIAN_FRONTEND="noninteractive" \
	&& apt-get update \
	&& apt-get upgrade -y \
	&& apt-get install --no-install-recommends --no-install-suggests -y apt-utils locales \
	&& cp "/usr/share/zoneinfo/America/Sao_Paulo" /etc/localtime \
	&& localedef -i pt_BR -f UTF-8 pt_BR.UTF-8 \
	&& apt-get install --no-install-recommends --no-install-suggests -y \
		gettext-base ca-certificates unzip curl gnupg \
		apt-transport-https \
	&& apt-get clean \
	&& find /var/log -type f -delete \
	&& find /usr/share/i18n -type f -delete \
	&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/log/*.log /var/cache/debconf/*-old

COPY --from=bravado/supervisord:latest /usr/local/bin/supervisord /usr/local/bin/supervisord

ENV PUID 1000
ENV PGID 1000

ADD etc /etc

RUN chmod +x /etc/entrypoint.sh \
	&& chmod u+s /usr/local/bin/supervisord \
	&& useradd -U -m -d /home/app -s /bin/bash app

WORKDIR /home/app

USER app

ENTRYPOINT ["/etc/entrypoint.sh"]
