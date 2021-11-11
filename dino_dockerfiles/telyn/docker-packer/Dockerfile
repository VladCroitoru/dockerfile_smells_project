FROM golang:buster AS yaml2json

ADD https://github.com/buildkite/yaml2json/archive/master.zip ./
RUN apt update \
 && apt -y install unzip \
 && unzip master.zip \
 && cd yaml2json-master \
 && scripts/build \
 && mv dist/yaml2json-linux-amd64 /usr/bin/yaml2json \
 && apt clean \
 && rm -rf /var/lib/apt/lists/*


FROM debian:buster-slim

RUN apt-get update \
 && apt-get install -y \
      e2fsprogs \
      gzip \
      mount \
      qemu-utils \
      tar \
      unzip \
      wget

ADD https://releases.hashicorp.com/packer/1.6.4/packer_1.6.4_linux_amd64.zip ./


RUN unzip packer_1.6.4_linux_amd64.zip -d /bin

#yaml2json is a build of github.com/buildkite/yaml2json, included because we use yaml files becuase you can put comments in them.
COPY --from=yaml2json /usr/bin/yaml2json /usr/bin/yaml2json

ENTRYPOINT "/bin/bash"
