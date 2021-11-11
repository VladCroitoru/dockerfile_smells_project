FROM ubuntu:19.10 
ARG version="v1.14"
ARG urlrelease="https://github.com/patrickalin/bloomsky-client-go/releases/download"
RUN apt-get update
RUN apt-get -y  install wget
RUN wget $urlrelease/$version/config.yaml
RUN wget $urlrelease/$version/goBloomsky-linux-amd64.bin
RUN wget $urlrelease/$version/server.crt
RUN wget $urlrelease/$version/server.key
RUN chmod +x /goBloomsky-linux-amd64.bin
ENTRYPOINT /goBloomsky-linux-amd64.bin
