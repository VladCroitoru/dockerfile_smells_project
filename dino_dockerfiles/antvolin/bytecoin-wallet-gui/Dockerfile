FROM debian:latest

MAINTAINER antvolin@gmail.com

ARG USER_NAME

RUN printf 'path-exclude=/usr/share/locale/*\npath-exclude=/usr/share/doc/*\npath-include=/usr/share/locale/en/*' > /etc/dpkg/dpkg.cfg.d/purge && \
	apt-get update && apt-get install -y \
	wget unzip \
	libqt5widgets5 && \
	wget -q --content-disposition https://bytecoin.org/storage/wallets/bytecoin_wallet/bytecoin-desktop-20180219-beta-linux64.zip && \
	unzip *.zip -d /usr/local/bin/ && \
	rm *.zip && \
	apt-get purge -y wget unzip && \
	rm -rf /var/lib/apt/lists/*

RUN adduser --disabled-password --gecos '' $USER_NAME
USER $USER_NAME
WORKDIR /home/$USER_NAME

CMD ["bytecoin-gui"]
