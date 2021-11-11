FROM ubuntu:16.10

ENV SINUSBOT_VERSION 0.9.16-10f0fad
ENV TS3_VERSION 3.0.19.4
ENV YOUTUBEDL_VERSION 2017.01.02

RUN apt-get update \
	&& apt-get install -y x11vnc xvfb libxcursor1 ca-certificates bzip2 libglib2.0-0 libquazip-dev wget python \
	&& update-ca-certificates \
	&& useradd -u 3000 sinusbot \
	&& mkdir -p /sinusbot /sinusbot/TeamSpeak3-Client-linux_amd64/ \
	&& chown -R sinusbot:sinusbot /sinusbot \
	&& wget -q -O /usr/local/bin/youtube-dl https://github.com/rg3/youtube-dl/releases/download/$YOUTUBEDL_VERSION/youtube-dl \
	&& chmod 775 -f /usr/local/bin/youtube-dl

USER sinusbot
WORKDIR /sinusbot

RUN mkdir /sinusbot/data \
	&& wget https://www.sinusbot.com/pre/sinusbot-$SINUSBOT_VERSION.tar.bz2 \
	&& tar -xjf sinusbot-$SINUSBOT_VERSION.tar.bz2 \
	&& wget http://dl.4players.de/ts/releases/$TS3_VERSION/TeamSpeak3-Client-linux_amd64-$TS3_VERSION.run \
	&& chmod 0755 TeamSpeak3-Client-linux_amd64-$TS3_VERSION.run \
	&& tail -c +25000 TeamSpeak3-Client-linux_amd64-$TS3_VERSION.run | tar -xzf- -C TeamSpeak3-Client-linux_amd64/ \
	&& cp plugin/libsoundbot_plugin.so TeamSpeak3-Client-linux_amd64/plugins \
	&& chmod 755 sinusbot

ADD config.ini config.ini
EXPOSE 8087
VOLUME /sinusbot/data
ENTRYPOINT ./sinusbot
