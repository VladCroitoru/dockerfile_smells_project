FROM node

WORKDIR /srv

RUN curl https://get.docker.com/builds/Linux/x86_64/docker-1.12.1.tgz | tar zx -C /opt

RUN ln -s /opt/docker/docker /usr/bin/docker && docker -v

COPY package.json index.ts exec-docker.ts /srv/

RUN npm i

RUN node_modules/.bin/tsc index.ts

ENTRYPOINT [ "node", "index.js" ]
