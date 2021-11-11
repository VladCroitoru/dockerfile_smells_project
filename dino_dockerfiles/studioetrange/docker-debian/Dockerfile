FROM debian:stable
MAINTAINER StudioEtrange <nomorgan@gmail.com>

# Debian package & stuff -------------

RUN echo "deb http://httpredir.debian.org/debian stable main non-free" >> /etc/apt/sources.list \
	&& echo "deb http://httpredir.debian.org/debian-updates stable-updates main non-free" >> /etc/apt/sources.list
	&& echo "deb http://httpredir.debian.org/debian-backports stable-backports main non-free" >> /etc/apt/sources.list

# DEBIAN packages
RUN apt-get update \
	&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
						python \
						supervisor \
						unrar \
						unzip \
						curl \
						git \
 						ca-certificates \
						pwgen \
						wget \
						nano \
	&& rm -rf /var/lib/apt/lists/*


# SUPERVISOR -------------
COPY supervisord.conf /etc/supervisor/supervisord.conf

# Supervisord web interface -------
EXPOSE 9999


CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf", "-n"]
