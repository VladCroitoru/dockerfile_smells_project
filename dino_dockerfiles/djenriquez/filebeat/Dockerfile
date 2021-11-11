FROM alpine:3.6

ENV FILEBEAT_VERSION=5.6.2

RUN set -x \
 && apk add --update bash curl tar openssl \                    
 && curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-${FILEBEAT_VERSION}-linux-x86_64.tar.gz \
 && tar xzvf filebeat-${FILEBEAT_VERSION}-linux-x86_64.tar.gz -C /usr/local/bin/ --strip-components=1 \
 && rm -rf filebeat-${FILEBEAT_VERSION}-linux-x86_64.tar.gz \
 && apk --no-cache add ca-certificates \
 && wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://raw.githubusercontent.com/sgerrand/alpine-pkg-glibc/master/sgerrand.rsa.pub \
 && wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.23-r3/glibc-2.23-r3.apk \
 && wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.1.3/dumb-init_1.1.3_amd64 \
 && chmod +x /usr/local/bin/dumb-init \
 && apk add glibc-2.23-r3.apk \
 && apk del curl tar openssl \
 && rm -rf /var/cache/apk/*

COPY start.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/start.sh /usr/local/bin/filebeat

ENTRYPOINT ["start.sh"]
