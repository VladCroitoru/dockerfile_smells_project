FROM alpine:edge
RUN apk upgrade --no-cache \
 && apk add --no-cache libsodium libevent make autoconf gcc musl-dev bsd-compat-headers libevent-dev libsodium-dev supervisor \
 && wget -O- https://github.com/cofyc/dnscrypt-wrapper/archive/v0.4.2.tar.gz | tar -xz \
 && cd dnscrypt-wrapper-0.4.2/ \
 && make \
 && make install \
 && cd .. \
 && rm -rf dnscrypt-wrapper-0.4.2/
ADD files /
ENV DNSCRYPT_HOST_PORTS="0.0.0.0 8443" \
    DNSCRYPT_HOSTS="127.0.0.1 127.0.0.2 127.0.0.3" \
    DNSCRYPT_PORTS="8443 12345 27015" \
    DNSCRYPT_CERT_FILE_EXPIRE_DAYS="1h" \
    DNSCRYPT_CERT_FILE_ROTATION_INTERVAL="3300" \
    DNSCRYPT_CERT_FILE_ROTATION_TIMEOUT="300" \
    DNSCRYPT_CERT_FILE_HISTORY_SIZE="24" \
    DNSCRYPT_PROVIDER_NAME="dnscrypt.info" \
    DNSCRYPT_RESOLVER_ADDRESS="127.0.0.1:53"
CMD ["/boot.sh"]
