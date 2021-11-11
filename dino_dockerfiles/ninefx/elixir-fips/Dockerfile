FROM ninefx/erlang-fips:22.3

# elixir expects utf8.
ENV ELIXIR_VERSION="v1.10.2" \
    LANG=C.UTF-8

RUN set -xe \
    && ELIXIR_DOWNLOAD_URL="https://github.com/elixir-lang/elixir/archive/${ELIXIR_VERSION}.tar.gz" \
    && ELIXIR_DOWNLOAD_SHA256="c12a4931a5383a8a9e9eb006566af698e617b57a1f645a6cb132a321b671292d" \
    && apk --update add --no-cache wget curl make git openssh tar gzip ca-certificates \
    && wget --quiet $ELIXIR_DOWNLOAD_URL \
    && openssl dgst -sha256 ${ELIXIR_VERSION}.tar.gz | grep $ELIXIR_DOWNLOAD_SHA256 \
    && tar xfz ${ELIXIR_VERSION}.tar.gz \
    && rm ${ELIXIR_VERSION}.tar.gz \
    && cd elixir* \
    && make test install clean \
    && cd .. \
    && rm -rf elixir* \
    && apk del --purge wget curl make

CMD ["iex"]