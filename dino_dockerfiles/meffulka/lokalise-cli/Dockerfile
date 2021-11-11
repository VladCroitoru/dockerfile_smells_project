FROM alpine:3.7

LABEL maintainer="Alekseii Erokhin <zmeffulka@gmail.com>"

RUN apk add --no-cache git coreutils openssh zip python && \
    python -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip install --upgrade pip setuptools && \
    rm -r /root/.cache

COPY lokalise /usr/local/bin/

RUN chmod 755 /usr/local/bin/lokalise

CMD /bin/sh
