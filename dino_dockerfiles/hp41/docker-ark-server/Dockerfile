FROM ubuntu:16.04
ENV TINI_VERSION v0.15.0
ENV PATH "/home/steam/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN apt-get update && \ 
    apt-get -y install perl-modules curl lsof libc6-i386 lib32gcc1 bzip2 unzip vim sudo && \
    useradd -m steam && \
    chmod +x /tini

ENTRYPOINT ["/tini", "-v", "--", "/entrypoint.sh"]
CMD ["run"]

WORKDIR /home/steam
VOLUME /home/steam
ADD entrypoint.sh /
RUN chmod +x /entrypoint.sh 
USER steam
