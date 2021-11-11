FROM ruby:2.3.0-slim

# Install dev tools
RUN apt-get update && \
    apt-get install \
        --no-install-recommends \
        -y \
        build-essential \
        fontforge \
        unzip \
        wget \
    && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    wget http://people.mozilla.com/~jkew/woff/woff-code-latest.zip && \
    unzip woff-code-latest.zip -d sfnt2woff && \
    cd sfnt2woff && \
    make && \
    mv sfnt2woff /usr/local/bin/ && \
    cd .. && \
    rm -rf sfnt2woff woff-code-latest.zip && \
    gem install fontcustom && \
    apt-get purge -y --auto-remove \
        build-essential \
        unzip \
        wget

VOLUME ["/fontcustom"]
WORKDIR /fontcustom

ENTRYPOINT ["fontcustom"]
