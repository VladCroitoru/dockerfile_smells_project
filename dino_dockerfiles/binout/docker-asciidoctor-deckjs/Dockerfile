FROM asciidoctor/docker-asciidoctor

MAINTAINER Benoit Prioux <benoit.prioux@gmail.com>

ENV TMP_DECKJS /tmp/deckjs

RUN mkdir $TMP_DECKJS \
    && (curl -LkSs https://api.github.com/repos/asciidoctor/asciidoctor-deck.js/tarball | tar xfz - -C $TMP_DECKJS --strip-components=1) \
    && mv $TMP_DECKJS/templates/haml/* $BACKENDS/haml/deckjs/

CMD ["/bin/bash"]
