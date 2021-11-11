FROM ubuntu:16.04
ENV ELM_VERSION='0.17.0'

RUN apt update && \
    apt-get install -y git curl && \
    curl -L "https://caddyserver.com/download/build?os=linux&arch=amd64&features=git%2Chugo%2Cprometheus" -o caddy.tar.gz && \
    curl -L "https://dl.bintray.com/elmlang/elm-platform/${ELM_VERSION}/linux-x64.tar.gz" -o elm.tar.gz && \
    tar xzf caddy.tar.gz -C /tmp && \
    tar xzf elm.tar.gz -C /tmp && \
    mv /tmp/caddy /usr/local/bin/caddy && \
    mv /tmp/dist_binaries/* /usr/local/bin/ && \
    rm -f caddy.tar.gz && \
    rm -f elm.tar.gz && \
    rm -rf /tmp/caddy && \
    rm -rf /tmp/dist_binaries && \
    mkdir -p /app && \
    apt clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY Caddyfile.run /app/Caddyfile

WORKDIR /app
CMD ["caddy"]
