FROM mhart/alpine-node:12.13.1

#Install packages
RUN apk update \
	&& apk add bash gcc g++ make python git openssh && rm -rf /var/cache/apk/*

RUN npm install -g node-gyp
RUN npm install -g npm-start

WORKDIR /docker
COPY startup.sh .

# give all execution rights
RUN chmod a+x startup.sh

RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/community >> /etc/apk/repositories
RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/main >> /etc/apk/repositories
RUN apk add --no-cache w3m p7zip jq

WORKDIR /docker/src

ENTRYPOINT ["bash","/docker/startup.sh"]


