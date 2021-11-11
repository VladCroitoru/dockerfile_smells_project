FROM resin/raspberrypi3-alpine

LABEL maintainer="joseba.io"

ENV LEANOTE_VERSION 2.5

RUN [ "cross-build-start" ]

ADD https://sourceforge.net/projects/leanote-bin/files/2.5/leanote-linux-arm-v${LEANOTE_VERSION}.bin.tar.gz/download /usr/local

RUN tar -xzvf /usr/local/download -C /usr/local && \
    rm -f /usr/local/download

RUN chmod +x /usr/local/leanote/bin/run.sh

RUN hash=$(< /dev/urandom tr -dc A-Za-z0-9 | head -c${1:-64};echo;); \
    sed -i "s/app.secret=.*$/app.secret=$hash #/" /usr/local/leanote/conf/app.conf; \
    sed -i "s/db.host=.*$/db.host=mongodb/" /usr/local/leanote/conf/app.conf; \
    sed -i "s/site.url=.*$/site.url=\${SITE_URL} /" /usr/local/leanote/conf/app.conf;

RUN [ "cross-build-end" ]

EXPOSE 9000
WORKDIR  /usr/local/leanote/bin
ENTRYPOINT ["sh", "run.sh"]