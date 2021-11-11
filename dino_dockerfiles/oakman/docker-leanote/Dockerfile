FROM alpine:3.5

RUN apk --update add curl && \
    curl -L http://sourceforge.net/projects/leanote-bin/files/2.4/leanote-linux-amd64-v2.4.bin.tar.gz/download >> \
    /usr/local/leanote-linux-amd64.bin.tar.gz && \
    apk del --purge curl && \
    rm -rf /var/cache/apk/*

RUN tar -xzvf /usr/local/leanote-linux-amd64.bin.tar.gz -C /usr/local
RUN chmod +x /usr/local/leanote/bin/run.sh
RUN hash=$(< /dev/urandom tr -dc A-Za-z0-9 | head -c${1:-64};echo;); \
    sed -i "s/app.secret=.*$/app.secret=$hash #/" /usr/local/leanote/conf/app.conf; \
    sed -i "s/db.host=.*$/db.host=db/" /usr/local/leanote/conf/app.conf; \
    sed -i "s/site.url=.*$/site.url=\${SITE_URL} /" /usr/local/leanote/conf/app.conf;

EXPOSE 9000
WORKDIR  /usr/local/leanote/bin
ENTRYPOINT ["sh", "run.sh"]