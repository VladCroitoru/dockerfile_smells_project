FROM alpine:edge

RUN apk add --no-cache python3 \
                       python3-dev \
                       build-base \
                       git \
                       ca-certificates && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    ln -s /usr/include/locale.h /usr/include/xlocale.h && \
    pip3 install --upgrade pip setuptools \
                               numpy \
                               pandas \
                               xlrd \
                               dicttoxml && \
    apk del python3-dev \
            build-base \
            git && \
    rm -r /root/.cache

COPY ./excel2xml.py /excel2xml.py

WORKDIR /pwd

ENTRYPOINT ["/usr/bin/python3", "/excel2xml.py"]

CMD ["--help"]
