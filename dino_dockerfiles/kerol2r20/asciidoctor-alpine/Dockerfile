FROM alpine

MAINTAINER Yu-Hsin Lu <kerol2r20@gmail.com>

WORKDIR /src

RUN apk add -U ruby ruby-bundler graphviz openjdk8 ruby-json ruby-rake ruby-dev ttf-dejavu && \
    gem install --no-ri asciidoctor asciidoctor-pdf-cjk-kai_gen_gothic asciidoctor-diagram && \
    gem install --no-ri asciidoctor-pdf --pre && \
    asciidoctor-pdf-cjk-kai_gen_gothic-install && \
    apk add build-base cmake bison flex libffi-dev libxml2-dev gdk-pixbuf-dev pango-dev cairo-dev lasem-dev=0.5.0-r2 && \
    ln -s /usr/lib/liblasem-0.6.so /usr/lib/liblasem.so && \
    gem install --no-ri asciidoctor-mathematical

CMD ["/bin/sh"]