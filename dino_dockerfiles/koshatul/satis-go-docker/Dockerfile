FROM composer/satis:latest

ENV SATIS_GO_BIND 0.0.0.0:8080
ENV SATIS_GO_DB_PATH /opt/satis-go/data
ENV SATIS_GO_REPOUI_PATH /usr/share/nginx/htlm
ENV SATIS_GO_REPO_NAME "My Satis"
ENV SATIS_GO_REPO_HOST http://localhost:8080
ENV SATIS_GO_USERNAME ""
ENV SATIS_GO_PASSWORD ""
ENV PATH="/satis/bin:${PATH}"

# based on https://github.com/frol/docker-alpine-glibc/blob/alpine-3.4/Dockerfile
# also added envsubst based on https://github.com/cirocosta/alpine-envsubst/blob/master/Dockerfile
RUN ALPINE_GLIBC_BASE_URL="https://github.com/sgerrand/alpine-pkg-glibc/releases/download" && \
    ALPINE_GLIBC_PACKAGE_VERSION="2.23-r3" && \
    ALPINE_GLIBC_BASE_PACKAGE_FILENAME="glibc-$ALPINE_GLIBC_PACKAGE_VERSION.apk" && \
    ALPINE_GLIBC_BIN_PACKAGE_FILENAME="glibc-bin-$ALPINE_GLIBC_PACKAGE_VERSION.apk" && \
    ALPINE_GLIBC_I18N_PACKAGE_FILENAME="glibc-i18n-$ALPINE_GLIBC_PACKAGE_VERSION.apk" && \
    apk add --update libintl && \
    apk add --virtual=.build-dependencies wget ca-certificates gettext && \
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
    cp /usr/bin/envsubst /usr/local/bin/envsubst && \
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
        "$ALPINE_GLIBC_I18N_PACKAGE_FILENAME" && \
    rm -rf /var/cache/apk/*

# install satis-go
RUN mkdir -p /opt/satis-go && \
    wget -qO- https://github.com/koshatul/satis-go/releases/download/0.1.2/satis-go-linux-amd64.tar.gz | \
    tar xvfz - -C /opt/satis-go/ && \
    chmod +x /opt/satis-go/satis-go && \
    wget -qO-  https://github.com/benschw/satis-admin/releases/download/0.1.1/admin-ui.tar.gz | \
        tar xzv -C /opt/satis-go/

ADD entrypoint.sh /entrypoint.sh
ADD config.template.yaml /opt/satis-go/config.template.yaml
ADD ssh_config /root/.ssh/config

EXPOSE 8080

ENTRYPOINT ["/entrypoint.sh"]

CMD ["/opt/satis-go/satis-go"]
