# based on Martijn Koster's "https://github.com/makuk66/docker-oracle-java7"
# based on Stéphane Cottin 

FROM vixns/java8
MAINTAINER Michał Zubkowicz <michal.zubkowicz@gmail.com>

RUN \
    export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get -y install imagemagick && \
    apt-get -y install gifsicle && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


