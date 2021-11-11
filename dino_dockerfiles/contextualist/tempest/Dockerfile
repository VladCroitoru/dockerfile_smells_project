FROM alpine:latest

ENV CONF_DIR="/usr/local/conf" \
    KCPTUN_DIR="/usr/local/kcp-server" \
    SS_SCRIPT="https://github.com/shadowsocks/shadowsocks-libev/raw/master/docker/alpine/Dockerfile" \
    SS_URL="https://glare.now.sh/shadowsocks/shadowsocks-libev/.*gz"

RUN set -ex && \
    apk add --no-cache curl && \
    curl -sSL ${SS_SCRIPT} | sed -n '/RUN/{p; :loop; n; /USER/q; p; bloop;}' | sed -e '1s/RUN/   /' | ash && \
    mkdir -p ${CONF_DIR} && \
    mkdir -p ${KCPTUN_DIR} && \
    apk add --no-cache bash \
                       curl \
                       openssh \
                       tar && \
    sed -i s/#PermitRootLogin.*/PermitRootLogin\ yes/ /etc/ssh/sshd_config && \
    rm -rf /var/cache/apk/* ~/.cache


ADD *.sh /
RUN chmod +x /*.sh

EXPOSE 22
EXPOSE 29900/udp
ENTRYPOINT ["/entrypoint.sh"]
