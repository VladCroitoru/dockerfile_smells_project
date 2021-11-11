FROM docker:1.12-dind

RUN apk --update add curl git jq rsync openssh

# add glibc https://github.com/frol/docker-alpine-glibc/blob/master/Dockerfile
RUN ALPINE_GLIBC_BASE_URL="https://github.com/sgerrand/alpine-pkg-glibc/releases/download" && \
    ALPINE_GLIBC_PACKAGE_VERSION="2.23-r3" && \
    ALPINE_GLIBC_BASE_PACKAGE_FILENAME="glibc-$ALPINE_GLIBC_PACKAGE_VERSION.apk" && \
    ALPINE_GLIBC_BIN_PACKAGE_FILENAME="glibc-bin-$ALPINE_GLIBC_PACKAGE_VERSION.apk" && \
    ALPINE_GLIBC_I18N_PACKAGE_FILENAME="glibc-i18n-$ALPINE_GLIBC_PACKAGE_VERSION.apk" && \
    apk add --no-cache --virtual=.build-dependencies wget ca-certificates && \
    wget \
        "https://raw.githubusercontent.com/andyshinn/alpine-pkg-glibc/master/sgerrand.rsa.pub" \
        -O "/etc/apk/keys/sgerrand.rsa.pub" && \
    wget \
        "$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \
        "$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \
        "$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_I18N_PACKAGE_FILENAME" && \
    apk add --no-cache \
        "$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \
        "$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \
        "$ALPINE_GLIBC_I18N_PACKAGE_FILENAME" && \
    \
    rm "/etc/apk/keys/sgerrand.rsa.pub" && \
    /usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8 C.UTF-8 || true && \
    echo "export LANG=C.UTF-8" > /etc/profile.d/locale.sh && \
    \
    apk del glibc-i18n && \
    \
    rm "/root/.wget-hsts" && \
    apk del .build-dependencies && \
    rm \
        "$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \
        "$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \
        "$ALPINE_GLIBC_I18N_PACKAGE_FILENAME"
# modify entrypoint.sh
COPY docker-entrypoint.sh /usr/local/bin/

# entrykit
RUN curl -Ls https://github.com/progrium/entrykit/releases/ | \
  egrep -o '/progrium/.*entrykit_[0-9\.]+_Linux_x86_64.tgz' | head -1 | \
  (curl -Lo entrykit.tgz http://github.com/`cat`) \
  && tar xzf entrykit.tgz -C /bin \
  && rm entrykit.tgz \
  && chmod +x /bin/entrykit \
  && entrykit --symlink && entrykit -v

# sigli
RUN curl -Ls https://github.com/gliderlabs/sigil/releases | \
  egrep -o '/gliderlabs/sigil/.*sigil_[0-9\.]+_Linux_x86_64.tgz' | head -1 | \
  (curl -Lo sigil.tgz http://github.com/`cat`) \
  && tar xzf sigil.tgz -C /bin \
  && rm sigil.tgz && sigil -v

# docker-compose
RUN curl -s -L https://github.com/docker/compose/releases/latest | \
    egrep -o '/docker/compose/releases/download/[0-9.]*/docker-compose-Linux-x86_64' | \
    (curl -Lo /usr/local/bin/docker-compose http://github.com/`cat`) && \
    chmod +x /usr/local/bin/docker-compose && \
    /usr/local/bin/docker-compose --version

ENTRYPOINT ["dockerd-entrypoint.sh"]
CMD []

