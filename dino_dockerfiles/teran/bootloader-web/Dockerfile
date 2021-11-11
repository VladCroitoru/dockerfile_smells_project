FROM alpine:latest

ARG BUILD_DATE
ARG VCS_REF

LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/teran/bootloader-web.git" \
      org.label-schema.vcs-ref=$VCS_REF

EXPOSE 80
EXPOSE 443

ENV DJANGO_SETTINGS_MODULE=bootloader.settings

RUN adduser -SDHh /opt/bootloader/web -s /bin/sh bootloader

RUN apk --update --no-cache add \
      ca-certificates \
      libpq \
      mailcap \
      nginx \
      python \
      py2-pip \
      openssl && \
    rm -f /var/cache/apk/* && \
    rm -f /etc/nginx/conf.d/default.conf && \
    update-ca-certificates

RUN pip install --no-cache-dir --upgrade pip && \
    find / -name '*.pyc' -or -name '*.pyo' -delete

ADD bootloader/requirements.txt /opt/bootloader/web/requirements.txt

RUN apk add --update --no-cache \
      freetype-dev \
      g++ \
      gcc \
      linux-headers \
      pkgconfig \
      postgresql-dev \
      python-dev && \
    pip install --no-cache-dir --upgrade -r /opt/bootloader/web/requirements.txt && \
    pip install --no-cache-dir --upgrade uwsgi && \
    find / -name '*.pyc' -or -name '*.pyo' -delete && \
    apk del --update --purge --no-cache \
      freetype-dev \
      g++ \
      gcc \
      linux-headers \
      pkgconfig \
      postgresql-dev \
      python-dev

WORKDIR "/opt/bootloader/web"

ADD docker/uwsgi.yaml /etc/bootloader/uwsgi.yaml
ADD docker/nginx-http.conf /etc/bootloader/nginx-http.conf
ADD docker/nginx-ssl.conf /etc/bootloader/nginx-ssl.conf
ADD docker/nginx-http-redirect.conf /etc/bootloader/nginx-http-redirect.conf

ADD docker/entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

ADD bootloader /opt/bootloader/web
