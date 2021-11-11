FROM alpine:3.7

ENV UID 1000
ENV GID 1000
ENV USER htpc
ENV GROUP htpc

ENV JACKETT_VERSION 0.8.1209

ENV XDG_CONFIG_HOME /config/

RUN addgroup -S ${GROUP} -g ${GID} && adduser -D -S -u ${UID} ${USER} ${GROUP}  && \
    apk add --no-cache --update curl libcurl tar mono tzdata --update-cache --repository http://alpine.gliderlabs.com/alpine/edge/testing/ --allow-untrusted  && \
    curl -ssL https://curl.haxx.se/ca/cacert.pem | cert-sync /dev/stdin && \
    mkdir -p /opt/jackett /config/Jackett && curl -sL https://github.com/Jackett/Jackett/releases/download/v${JACKETT_VERSION}/Jackett.Binaries.Mono.tar.gz | tar xz -C /opt/jackett --strip-components=1 && \
    chown -R ${USER}:${GROUP} /config/ /opt/jackett/ && \
    apk del curl tar
   
EXPOSE 9117 

WORKDIR /opt/

VOLUME /config/Jackett

LABEL url=https://github.com/Jackett/Jackett/
LABEL version=${JACKETT_VERSION}

USER ${USER}

ENTRYPOINT ["mono", "jackett/JackettConsole.exe"]
