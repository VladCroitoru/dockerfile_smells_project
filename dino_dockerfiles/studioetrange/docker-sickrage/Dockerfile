FROM studioetrange/docker-debian:wheezy
MAINTAINER StudioEtrange <nomorgan@gmail.com>


# DEBIAN packages : SICKRAGE dependencies install ----------
RUN apt-get update \
	&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
						python-cheetah \
	&& rm -rf /var/lib/apt/lists/*
	

# SICKRAGE install -------------
ENV ITEM_VERSION v4.0.22

WORKDIR /opt/sickrage
RUN curl -k -SL "https://github.com/SiCKRAGETV/SickRage/archive/$ITEM_VERSION.tar.gz" \
	| tar -xzf - -C /opt/sickrage --strip-components=1

# SUPERVISOR -------------
COPY supervisord-sickrage.conf /etc/supervisor/conf.d/supervisord-sickrage.conf

# DOCKER -------------
VOLUME /data

# Supervisord web interface -------
EXPOSE 9999
# sickrage http port
EXPOSE 8081

# run command by default
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf", "-n"]
