FROM alpine:3.12 as builder

RUN apk add --no-cache --virtual .build-deps \
        build-base \
        cmake \
        boost-dev \
        openssl-dev \
        mariadb-connector-c-dev \
        wget

RUN wget -O - "https://api.github.com/repos/trojan-gfw/trojan/releases/latest" \
     | grep "tarball_url" | cut -d\" -f4 \
     | wget -O /tmp/trojan.tar.gz -i -

RUN tar -C /tmp -xf /tmp/trojan.tar.gz \
    && cd /tmp/trojan-gfw* \
    && cmake . \
    && make -j $(nproc) \
    && strip -s trojan \
    && mv trojan /tmp

FROM alpine:3.12

RUN apk add --no-cache --virtual .trojan-rundeps \
    libstdc++ \
    boost-system \
    boost-program_options \
    mariadb-connector-c

COPY --from=builder /tmp/trojan /usr/local/bin

WORKDIR /etc/trojan

CMD ["trojan", "-l", "/var/log/trojan.log", "-c", "config.json"]
