FROM alpine

LABEL maintainer="letssudormrf"

#Download applications
RUN set -ex \
    && if [ $(wget -qO- ipinfo.io/country) == CN ]; then echo "http://mirrors.aliyun.com/alpine/latest-stable/main/" > /etc/apk/repositories ;fi \
    && apk --update add --no-cache libsodium python git

#Execution environment
COPY entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh

EXPOSE 8443/tcp 8443/udp

WORKDIR /tmp

VOLUME ["/tmp"]

CMD ["entrypoint.sh"]
