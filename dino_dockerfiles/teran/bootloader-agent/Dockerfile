FROM alpine:latest

ARG BUILD_DATE
ARG VCS_REF

LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/teran/bootloader-agent.git" \
      org.label-schema.vcs-ref=$VCS_REF

EXPOSE 67/udp
EXPOSE 69/udp
EXPOSE 80

RUN adduser -SDHh /opt/bootloader/agent -s /bin/sh bootloader

RUN apk --update --no-cache add \
      ca-certificates \
      dnsmasq \
      nginx \
      python \
      py2-pip \
      openssl && \
    rm -vf /var/cache/apk/* && \
    pip install --no-cache-dir --upgrade pip && \
    update-ca-certificates

RUN mkdir -p \
      /var/lib/tftp/pxelinux.cfg \
      /var/lib/http && \
    chown -R bootloader:nogroup /var/lib/tftp /var/lib/http

RUN apk add --update --no-cache syslinux && \
    cp /usr/share/syslinux/pxelinux.0 /var/lib/tftp/pxelinux.0 && \
    cp /usr/share/syslinux/lpxelinux.0 /var/lib/tftp/lpxelinux.0 && \
    cp /usr/share/syslinux/ldlinux.c32 /var/lib/tftp/ldlinux.c32 && \
    apk del --update --purge --no-cache syslinux && \
    rm -f /var/cache/apk/*


WORKDIR "/opt/bootloader/agent"

RUN pip install --no-cache-dir --upgrade pip && \
    find / -name '*.pyc' -or -name '*.pyo' -delete

ADD requirements.txt /opt/bootloader/agent/

RUN apk add --update --no-cache \
      freetype-dev \
      g++ \
      gcc \
      git \
      linux-headers \
      pkgconfig \
      python-dev && \
    pip install --no-cache-dir --upgrade -r /opt/bootloader/agent/requirements.txt && \
    find / -name '*.pyc' -or -name '*.pyo' -delete && \
    apk del --update --purge --no-cache \
      freetype-dev \
      g++ \
      gcc \
      git \
      linux-headers \
      pkgconfig \
      python-dev

RUN mkdir -p /var/lib/bootloader/callback

ADD docker/nginx.conf /etc/nginx/nginx.conf
ADD docker/uwsgi.yaml /etc/bootloader/uwsgi.yaml

ADD docker/entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

ADD deployments /opt/bootloader/agent/deployments
