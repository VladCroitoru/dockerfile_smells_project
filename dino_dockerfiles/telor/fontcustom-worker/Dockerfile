FROM ubuntu:16.04

ENV FONTCUSOM_VERSION 2.0.0

RUN apt-get update && \
    apt-get -y install ruby ruby-dev fontforge wget build-essential zlib1g-dev unzip eot-utils python git woff-tools && \
    git clone https://github.com/bramstein/sfnt2woff-zopfli.git sfnt2woff-zopfli && cd sfnt2woff-zopfli && \
    make && \
    mv sfnt2woff-zopfli /usr/local/bin/sfnt2woff && \
    git clone --recursive https://github.com/google/woff2.git && \
    cd woff2 && \
    make clean all && \
    mv woff2_compress /usr/local/bin/ && \
    mv woff2_decompress /usr/local/bin/ && \
    gem install --no-document fontcustom -v "${FONTCUSOM_VERSION}"

VOLUME /app/project

WORKDIR /app/project

CMD ["fontcustom", "help"]
