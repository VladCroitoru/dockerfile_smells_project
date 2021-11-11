FROM  mhart/alpine-node:4

ENV MACHINE_VERSION=v0.5.3

ADD . /neptune-back
WORKDIR neptune-back

RUN apk add --update curl \
  && curl -L https://github.com/docker/machine/releases/download/${MACHINE_VERSION}/docker-machine_linux-amd64 >/usr/local/bin/docker-machine \
	&& chmod +x /usr/local/bin/docker-machine \
  && npm run build \
  && apk del curl \
	&& rm -rf /var/cache/apk/*

EXPOSE 3000

ENTRYPOINT ["npm", "run", "start"]
