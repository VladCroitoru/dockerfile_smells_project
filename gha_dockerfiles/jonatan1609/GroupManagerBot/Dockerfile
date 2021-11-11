FROM python:3.9.7-alpine

USER root
ENV PYTHONUNBUFFERED=1

RUN \
addgroup -S bot \
&& adduser -DHS -G bot bot \
&& mkdir -p /config \
  && chown -R bot:bot /config \
  && chmod -R 775 /config \
&& apk add --no-cache \
            tini git

WORKDIR /opt/bot
COPY . /opt/bot/

RUN \
pip install --no-cache-dir -r requirements.txt \
&& mv /opt/bot/.config.toml.example /opt/bot/.config.toml.example \
&& chown -R bot:bot /opt/bot

USER bot
VOLUME [ "/config" ]
ENTRYPOINT ["/sbin/tini", "--"]

CMD ["/opt/bot/entrypoint.sh"]

LABEL org.opencontainers.image.source https://github.com/jonatan1609
