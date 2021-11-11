FROM openhab/openhab:2.2.0-amd64-alpine

RUN apk add libcap \
  && setcap 'cap_net_raw,cap_net_admin,cap_net_bind_service=+eip' \
  $(realpath /usr/bin/java) \
  && ln -s /usr/lib/jvm/java-1.8-openjdk/lib/amd64/jli/libjli.so /usr/lib/ \
  && ln -s /usr/lib/jvm/java-1.8-openjdk/lib/amd64/libjava.so /usr/lib/ \
  && ln -s /usr/lib/jvm/java-1.8-openjdk/jre/lib/amd64/server/libjvm.so /usr/lib/ \
  && sync
