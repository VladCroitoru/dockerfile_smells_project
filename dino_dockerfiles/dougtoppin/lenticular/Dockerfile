FROM alpine
LABEL maintainer "dougtoppin@gmail.com"
LABEL org.label-schema.vcs-url="https://github.com/dougtoppin/lenticular"
LABEL org.label-schema.description="Tool for creating lenticular images by combining two images"

COPY ./lenticulate.pl /tmp

WORKDIR /tmp

RUN [ "apk", "update" ]
RUN [ "apk", "add", "perl" ]
RUN [ "apk", "add", "perl-gd" ]

ENTRYPOINT [ "/tmp/lenticulate.pl" ]

