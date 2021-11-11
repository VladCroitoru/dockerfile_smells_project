FROM alpine:edge
LABEL maintainer="Ayhan Akilli"

ENV LANG=de_DE.UTF-8
ENV MUSL_LOCPATH=/usr/share/i18n/locales/musl
ENV TZ=Europe/Berlin

COPY bin/ /usr/local/bin/
RUN echo 'https://dl-cdn.alpinelinux.org/alpine/edge/testing' >> /etc/apk/repositories && \
    apk add --no-cache \
        ca-certificates \
        musl-locales \
        musl-locales-lang \
        su-exec \
        tzdata && \
    app-dir && \
    app-user && \
    app-timezone
COPY init/ /init/

ENTRYPOINT ["app-entry"]
CMD ["su-exec", "app", "sh"]
