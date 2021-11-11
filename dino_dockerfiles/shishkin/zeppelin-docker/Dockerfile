FROM java:8-alpine

ENV ZEPPELIN_VERSION 0.6.0
ENV ZEPPELIN_URL http://www.apache.org/dist/zeppelin/zeppelin-$ZEPPELIN_VERSION/zeppelin-$ZEPPELIN_VERSION-bin-netinst.tgz

RUN set -x \
  && mkdir -p /zeppelin \
  && cd /zeppelin \
  && apk add --update --no-cache curl gnupg tar bash \
  && curl -fL $ZEPPELIN_URL -o zeppelin.tgz \
  && curl -fL $ZEPPELIN_URL.asc -o zeppelin.tgz.asc \
  && curl -fL https://www.apache.org/dist/zeppelin/KEYS -o KEYS \
  && gpg --import KEYS \
  && gpg --verify zeppelin.tgz.asc zeppelin.tgz \
  && tar -xvf zeppelin.tgz --strip-components=1 \
  && apk del curl gnupg \
  && rm zeppelin.tgz zeppelin.tgz.asc KEYS

VOLUME /zeppelin/conf
VOLUME /zeppelin/notebook
VOLUME /zeppelin/logs

EXPOSE 8080 8081

CMD /zeppelin/bin/zeppelin.sh

