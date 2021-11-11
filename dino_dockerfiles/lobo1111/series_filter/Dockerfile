FROM dahlb/alpine-flexget

COPY config.yml /opt/flexget/config.yml

ENV SLEEP 300

VOLUME /opt/complete
VOLUME /opt/storage

COPY start.sh /opt/
RUN chmod +x /opt/start.sh

WORKDIR /opt/
ENTRYPOINT ./start.sh
