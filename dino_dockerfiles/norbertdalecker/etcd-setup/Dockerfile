FROM alpine:3.1
RUN apk --update add curl tar bash wget openssl ca-certificates jq py-pip && pip install jsonpipe pyyaml
#apt-get install python-jsonpipe
RUN wget --no-check-certificate https://github.com/jwilder/dockerize/releases/download/v0.2.0/dockerize-linux-amd64-v0.2.0.tar.gz
RUN tar -C /usr/local/bin -xzvf dockerize-linux-amd64-v0.2.0.tar.gz

COPY ./docker-entrypoint.sh ./docker-entrypoint.sh
COPY ./bin/etcd-setup.sh ./etcd-setup.sh

CMD ./docker-entrypoint.sh
