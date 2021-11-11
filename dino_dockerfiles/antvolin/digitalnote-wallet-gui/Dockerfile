FROM debian:latest

MAINTAINER antvolin@gmail.com

ARG USER_NAME

WORKDIR /digitalnote-work

ADD https://github.com/xdn-project/digitalnotewallet/releases/download/v1.0.13-beta/digitalnotewallet-1.0.13-beta-136.amd64.deb .

RUN printf 'path-exclude=/usr/share/locale/*\npath-exclude=/usr/share/doc/*\npath-include=/usr/share/locale/en/*' > /etc/dpkg/dpkg.cfg.d/purge && \
	apt-get update && apt-get install -y \
	libqt5core5a \
	libqt5gui5 \
	libqt5network5 \
	libqt5widgets5 && \
	dpkg -i digitalnotewallet-1.0.13-beta-136.amd64.deb && \
	rm -rf /var/lib/apt/lists/*

RUN adduser --disabled-password --gecos '' $USER_NAME
USER $USER_NAME
WORKDIR /home/$USER_NAME

CMD ["digitalnotewallet"]
