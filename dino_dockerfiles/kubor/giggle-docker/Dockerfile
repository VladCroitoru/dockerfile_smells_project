FROM alpine:3.7

RUN apk update \
    && apk add gcc g++ make autoconf automake git zlib-dev \
        bzip2-dev curl-dev openssl-dev ruby libmicrohttpd-dev libtool

RUN git clone https://github.com/ryanlayer/giggle.git \
    && cd giggle \
    && make \
    && make server

ENV GIGGLE_ROOT="/giggle" PATH="/giggle/bin/:$PATH"

CMD [ 'giggle' ]
