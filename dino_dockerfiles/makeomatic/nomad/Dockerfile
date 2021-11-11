FROM frolvlad/alpine-glibc:alpine-3.9_glibc-2.29

LABEL vendor=makeomatic \
      version_tags="[\"0.8\",\"0.8.7\"]"

ENV NOMAD_VERSION=0.8.7 \
    NOMAD_SHA256=a5a3a507ee8048ab2337427824b5e7fd0c6c069ca5d2f545f13f742af0a707da

RUN apk --no-cache --update add curl libtool coreutils tzdata

RUN curl -sSL -o /tmp/nomad.zip https://releases.hashicorp.com/nomad/${NOMAD_VERSION}/nomad_${NOMAD_VERSION}_linux_amd64.zip && \
    echo "${NOMAD_SHA256}  /tmp/nomad.zip" | sha256sum -c - && unzip /tmp/nomad.zip -d /usr/local/bin && \
    rm -rf /tmp/*

VOLUME ["/data", "/config"]

# http server: 4646 (applies to server+client)
# rpc raft: 4647 (applies to server+client)
# serf gossip: 4648 TCP+UDP (applies to server)

EXPOSE 4646 4647 4648

ADD entrypoint.sh /

ENTRYPOINT ["/entrypoint.sh"]
