FROM node:10.13.0-alpine
LABEL maintainer="opensource@programator.sk"
RUN  apk update --no-cache && apk add ca-certificates curl rsync openssh-client git bash python make build-base && \
     npm i -g yarn && \ 
     mkdir -p ~/.ssh && \
     chmod 700 ~/.ssh && \
     echo -e "Host *\n\tStrictHostKeyChecking no\n\n" > ~/.ssh/config
ADD ./assets-version.sh /root
RUN sed -i '/mozilla\/DST_Root_CA_X3.crt/d' /etc/ca-certificates.conf
RUN update-ca-certificates --fresh
WORKDIR /root
