FROM studioetrange/docker-debian:wheezy
MAINTAINER StudioEtrange <nomorgan@gmail.com>


# DEBIAN packages : SICKBEARD dependencies install ----------
RUN apt-get update \
	&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
						python-cheetah \
	&& rm -rf /var/lib/apt/lists/*
	

# SICKBEARD install -------------
ENV ITEM_VERSION build-507

WORKDIR /opt/sickbeard

RUN curl -k -SL "https://github.com/midgetspy/Sick-Beard/archive/$ITEM_VERSION.tar.gz" \
	| tar -xzf - -C /opt/sickbeard --strip-components=1


# SUPERVISOR -------------
COPY supervisord-sickbeard.conf /etc/supervisor/conf.d/supervisord-sickbeard.conf

# DOCKER -------------
VOLUME /data

# Supervisord web interface -------
EXPOSE 9999
# sickbeard http port
EXPOSE 8081

# run command by default
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf", "-n"]
