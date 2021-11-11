FROM alpine:3.7

ENV SYNCTHING_VERSION=v0.14.45
ENV STNOUPGRADE=TRUE

# Add local files to image
COPY files /
    
RUN set -ex;\
    apk update;\
    apk upgrade;\
    apk add --no-cache su-exec tini curl;\
    rm -rf /var/cache/apk/*;\
    echo "*** Add syncthing system account ***";\
    addgroup -S syncthing;\
    adduser -S -D -h /home/syncthing -s /bin/false -G syncthing -g "syncthing system account" syncthing;\
    chown -R syncthing /home/syncthing

# Syncthing
RUN set -ex;\
    echo "Installing Syncthing ${SYNCTHING_VERSION} ...";\
    mkdir /opt;\
    curl -sSL --retry 1 https://github.com/syncthing/syncthing/releases/download/${SYNCTHING_VERSION}/syncthing-linux-amd64-${SYNCTHING_VERSION}.tar.gz | tar -C /opt -xvz;\
    ln -s /opt/syncthing-linux-amd64-${SYNCTHING_VERSION}/syncthing /usr/local/bin;\
    chmod -R +x /usr/local/bin

EXPOSE 8384 22000 21027/udp

ENTRYPOINT ["/sbin/tini", "--", "entrypoint.sh"]
CMD ["/usr/local/bin/syncthing", "-no-browser", "-no-restart", "-gui-address=0.0.0.0:8384", "-verbose"]
