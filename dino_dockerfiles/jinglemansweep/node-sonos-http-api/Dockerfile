FROM mhart/alpine-node:latest

ARG pkg_version="v1.0.1"
ARG package_url="https://github.com/jishi/node-sonos-http-api/tarball/${pkg_version}"

ENV HTTP_PORT        5005
ENV HTTPS_PORT       5006
ENV ANNOUNCE_VOLUME  40
ENV VOICERSS_API_KEY ""

RUN apk update && \
    apk add ca-certificates tar wget && \
    update-ca-certificates

ADD ./entrypoint.sh /

RUN mkdir -p /opt/app && \
    wget -q ${package_url} -O /tmp/package.tar.gz && \
    tar xzf /tmp/package.tar.gz --strip-components=1 -C /opt/app && \
    chmod +x /entrypoint.sh

WORKDIR /opt/app/
RUN npm install --production

EXPOSE 3500 ${HTTP_PORT} ${HTTPS_PORT}
VOLUME ["/opt/app/cache", "/opt/app/presets"]

ENTRYPOINT ["/entrypoint.sh"]

