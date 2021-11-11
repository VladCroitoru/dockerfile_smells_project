FROM alpine:3.6@sha256:1072e499f3f655a032e88542330cf75b02e7bdf673278f701d7ba61629ee3ebe

RUN apk add --update curl jq && \
    rm -rf /var/cache/apk/*

ENV release=

RUN set -x \
    && mkdir /var/syncthing \
    && mkdir /syncthing \
    && cd /syncthing \
    && release=${release:-$(curl -s https://api.github.com/repos/syncthing/syncthing/releases/latest | jq -r .tag_name )} \
    && curl -s -L https://github.com/syncthing/syncthing/releases/download/${release}/syncthing-linux-amd64-${release}.tar.gz \
    | tar -zx \
    && mv syncthing-linux-amd64-${release}/syncthing . \
    && rm -rf syncthing-linux-amd64-${release}

ENV STNOUPGRADE=1
ENTRYPOINT ["/syncthing/syncthing", "-home", "/var/syncthing/config", "-gui-address", "0.0.0.0:8384"]
