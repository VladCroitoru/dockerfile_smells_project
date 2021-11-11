FROM lsiobase/alpine.python:3.8

# set maintainer label
LABEL maintainer="fish2"

# install app
RUN git clone --depth 1 https://github.com/Fish2/PlexConnect /app/plexconnect

# add local files
COPY root/ /

# ports and volumes
EXPOSE 80 443 53
VOLUME /config
HEALTHCHECK --interval=1m --timeout=5s --retries=3 \
  CMD curl -sSL -D - localhost -o /dev/null || exit 1
