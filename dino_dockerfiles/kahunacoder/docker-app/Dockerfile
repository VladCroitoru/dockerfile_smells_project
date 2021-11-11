#FROM scratch
FROM debian:jessie
MAINTAINER "Gary Smith" <docker@kc.gs>

RUN apt-get update && apt-get install -y \
		curl \
		git \
        wget	\    
		sqlite3	\
        file \
        unzip \
        dos2unix \
        tree \
        vim \
        htop \
        tmux \
        libsqlite3-dev \
        libnotify-bin \

	&& mkdir -p /app_temp/app \
	&& mkdir -p /app_temp/logs \
	&& chown -R www-data /app_temp \
	&& chmod -R 1777 /app_temp
