FROM ocaml/opam:latest
LABEL maintainer "infiniteproject@gmail.com"

ENV DEBIAN_FRONTEND noninteractive
ENV PACKAGES "taglib mad lame vorbis cry liquidsoap"

RUN opam depext $PACKAGES && \
    opam install $PACKAGES

RUN sudo apt-get clean && \
    sudo rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY docker-entrypoint.sh /entrypoint.sh
RUN sudo chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
