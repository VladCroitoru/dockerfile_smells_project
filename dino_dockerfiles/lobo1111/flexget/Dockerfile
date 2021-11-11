FROM python:2.7

RUN pip install -I flexget

VOLUME /opt/flexget
VOLUME /opt/torrents

ENV TRAKT_USER trakt_user
ENV TRAKT_LIST flexget
ENV TIMEFRAME 1 hours
ENV QUALITY 720p
ENV SLEEP 300
ENV RSS http://default.com/rss
ENV CLUSTER_NAME default
ENV INSTANCE_NAME default

COPY start.sh /opt/
RUN chmod +x /opt/start.sh

COPY configManager opt/configManager/

WORKDIR /opt/
ENTRYPOINT ./start.sh
