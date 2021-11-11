FROM qnib/alplain-init:3.6 AS build

ARG RDK_VER=0.9.5
RUN apk --no-cache add g++ python ca-certificates yajl openssl make rsync
RUN mkdir -p /usr/local/librdkafka /usr/local/src \
 && wget -qO- https://github.com/edenhill/librdkafka/archive/v${RDK_VER}.tar.gz |tar xfz - -C /usr/local/src/ \
 && cd /usr/local/src/librdkafka-${RDK_VER} \
 && ./configure --prefix /usr/local/librdkafka \
 && make \
 && make install \
 && rsync -aP /usr/local/librdkafka/. /usr/local/
ARG KAFKACAT_VER=1.3.1
RUN mkdir -p /usr/local/kafkacat \
 && wget -qO- https://github.com/edenhill/kafkacat/archive/${KAFKACAT_VER}.tar.gz |tar xfz - -C /usr/local/src/ \
 && cd /usr/local/src/kafkacat-${KAFKACAT_VER} \
 && ./configure --enable-static --enable-json --prefix /usr/local/kafkacat \
 && make \
 && make install

FROM qnib/alplain-init:3.6
RUN apk --no-cache add ca-certificates yajl openssl yajl-dev
COPY --from=build /usr/local/librdkafka/lib/* /usr/local/lib/
COPY --from=build /usr/local/librdkafka/include/* /usr/local/include/
COPY --from=build /usr/local/kafkacat/bin/* /usr/local/bin/
CMD ["kafkacat", "-h"]
