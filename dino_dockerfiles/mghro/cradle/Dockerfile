FROM ubuntu:focal as builder
COPY scripts /scripts
WORKDIR /scripts
RUN /scripts/docker-setup.sh
COPY . /cradle
WORKDIR /cradle
RUN /scripts/docker-build.sh

FROM ubuntu:focal
RUN apt-get update && apt-get install -y curl
RUN curl -s -O https://curl.haxx.se/ca/cacert.pem && mv cacert.pem /usr/local/share/ca-certificates && update-ca-certificates
COPY --from=builder /cradle/build/deploy /cradle
COPY ./docker-config.json /root/.config/cradle/config.json
WORKDIR /cradle
VOLUME ["/var/cache/cradle"]
EXPOSE 41071
ENTRYPOINT ["/cradle/server"]
