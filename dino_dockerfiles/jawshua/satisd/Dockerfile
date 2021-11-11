FROM composer/satis
MAINTAINER jawshua@github

RUN wget https://github.com/Jawshua/satisd/releases/download/v0.1/satisd_0.1_linux_386.tar.gz \
    && tar zxvf satisd_0.1_linux_386.tar.gz \
    && mv satisd_0.1_linux_386/satisd /usr/local/bin/ \
    && rm -rf satisd_0.1_linux_386 satisd_0.1_linux_386.tar.gz

EXPOSE 80

CMD /usr/local/bin/satisd -satis /satis/bin/satis -config /satisd/config.json -repo /satisd/repo -listen :80

ENTRYPOINT ["/sbin/tini"]
