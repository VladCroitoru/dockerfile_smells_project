FROM ubuntu
MAINTAINER Laurens Stötzel <l.stoetzel@meeva.de>

RUN apt-get update -qqy && \
    apt-get install --no-install-recommends -qqy lsb-release && \
    \
    # Install OptiPNG
    echo "deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc) main universe" > /etc/apt/sources.list && \
    apt-get remove --purge -y lsb-release $(apt-mark showauto) && \
    apt-get update -qqy && \
    apt-get install -qqy --no-install-recommends optipng && \
    \
    # cleanup
    apt-get autoremove -y && \
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir -p /source
WORKDIR /source

ENTRYPOINT [ "/usr/bin/optipng" ]
CMD [ "-quiet", "-o7", "*.png" ]
