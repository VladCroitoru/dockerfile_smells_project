FROM alpine:edge

ENV version=0.38
ENV UID=1000
ENV GID=100

VOLUME ["/etc/motioneye", "/var/lib/motioneye"]
COPY entrypoint.sh /entrypoint.sh

RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories\
&&  apk --no-cache add\
    bash\
    motion\
    py2-pip\
    python\
    curl\
    openssl\
    tzdata\
&&  apk --no-cache add --virtual=buildreq\
    build-base\
    curl-dev\
    jpeg-dev\
    openssl-dev\
    python-dev\
    zlib-dev\
&&  pip install motioneye==$version\
&&  apk del buildreq\
&&  chmod +x /entrypoint.sh

CMD /entrypoint.sh /usr/bin/meyectl startserver -c /etc/motioneye/motioneye.conf

EXPOSE 8765
