FROM anapsix/alpine-java:8
MAINTAINER Shiaupiau <stu43005@gmail.com>

ENV HatH_PORT 11112

RUN apk update && \
    apk --no-cache add curl sqlite unzip && \
    mkdir -p /hath && \
    cd /hath && \
    curl -fsSL https://repo.e-hentai.org/hath/HentaiAtHome_1.6.0.zip -o hath.zip && \
    echo -n "597f0ae2d114a86e021013b0146d59b1f2f8be2025bfae6b38c181515b795018  hath.zip" | sha256sum -c && \
    unzip hath.zip && \
    rm hath.zip && \
    apk del curl unzip && \
    mkdir -p /hath/cache && \
    mkdir -p /hath/data && \
    mkdir -p /hath/download && \
    mkdir -p /hath/log && \
    mkdir -p /hath/temp

ADD client/start.sh /hath/start.sh

RUN chmod +x /hath/start.sh

WORKDIR /hath
EXPOSE "$HatH_PORT"
VOLUME ["/hath/cache", "/hath/data", "/hath/download", "/hath/log", "/hath/temp"]
CMD ["/hath/start.sh"]
