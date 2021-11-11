# Dockerfile for Teamspeak3 Server
# https://www.spors.io/

FROM debian:stretch
LABEL maintainer="Leon Spors <dev@spors.io>"

LABEL org.label-schema.name="halfbax/docker-teamspeak"
LABEL org.label-schema.description="Automatically updating Teamspeak 3 server with mountable server data"
LABEL org.label-schema.schema-version="0.6"

ENV TS_USER="teamspeak" \
    TS_PATH="/usr/local/teamspeak"

# System preparations
RUN apt-get update && \
    apt-get install -y curl wget bzip2 && \
    adduser --home $TS_PATH --shell /bin/bash --disabled-login --gecos "" $TS_USER

# User setup
COPY entrypoint.sh $TS_PATH/
RUN chown teamspeak $TS_PATH/entrypoint.sh && \
    chmod +x $TS_PATH/entrypoint.sh

USER $TS_USER
WORKDIR $TS_PATH

EXPOSE 9987/udp 2010/udp 30033 10011 41144 2008

ENTRYPOINT ["/bin/bash", "entrypoint.sh"]
