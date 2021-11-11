FROM alpine:3.6

MAINTAINER Tomohisa Kusano <siomiz@gmail.com>

RUN apk add -U \
    libxslt \
    openssl \
    python

ENV SEARX_VERSION v0.12.0

# FIXME this somehow doesn't work on Docker Cloud build...
# Error is: can't stat '/opt/searx': Not a directory
# ADD https://github.com/asciimoo/searx/archive/v0.12.0.tar.gz /opt
# RUN mv /opt/searx-* /opt/searx

WORKDIR /opt/searx

COPY install.sh /

RUN /bin/sh /install.sh

USER searx

COPY . .

CMD ["/usr/bin/python", "searx/webapp.py"]

EXPOSE 8888

ENTRYPOINT ["/bin/sh", "/opt/searx/entrypoint.sh"]
