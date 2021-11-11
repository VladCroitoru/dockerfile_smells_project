FROM      ubuntu:trusty
MAINTAINER Dan Porter <dpreid@gmail.com>

# Get all required packages
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
        fontforge ttfautohint \
        wget tar build-essential \
        openjdk-7-jdk \
        git \
        unzip zlib1g-dev \
        libfreetype6-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Build everything
RUN mkdir -p /build && \
    \
    echo "ttf2eot build" && \
    cd /build && wget https://github.com/wget/ttf2eot/archive/v0.0.3.tar.gz && \
    tar zxvf v0.0.3.tar.gz && \
    cd /build/ttf2eot-0.0.3 && make && cp ttf2eot /usr/local/bin/ttf2eot && \
    \
    echo "woff build" && \
    cd /build && wget https://github.com/samboy/WOFF/archive/2017-06-11.tar.gz && \
    tar zxvf 2017-06-11.tar.gz && \
    cd /build/WOFF-2017-06-11 && make && cp sfnt2woff /usr/local/bin/sfnt2woff && \
    \
    echo "woff2 build" && \
    cd /build && git clone --recursive https://github.com/google/woff2.git woff2 && \
    cd woff2 && make clean all && cp woff2_* /usr/local/bin/ && \
    cd / && rm -rf /build

## CSS3FontConverter
RUN git clone https://github.com/zoltan-dulac/css3FontConverter /app && mkdir -p /fonts

WORKDIR /fonts

ADD run.sh /run.sh
RUN chmod 755 /run.sh

ENTRYPOINT ["/run.sh"]
