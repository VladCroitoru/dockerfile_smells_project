FROM docker-registry.default.svc:5000/phd-assess/node-base:latest

# not recommended by the Meteor guide, but still works:
RUN curl https://install.meteor.com/ | sh

# build-essential needed at build time, but not run time:
RUN set -e -x; export DEBIAN_FRONTEND=noninteractive; \
    apt -qy update; \
    apt -qy install build-essential git openssh-client

RUN mkdir -p /usr/src/app/
COPY . /usr/src/app/
WORKDIR /usr/src/app/
RUN meteor npm i && meteor npm run postinstall
RUN meteor build --allow-superuser /usr --directory
RUN cd /usr/bundle/programs/server && npm install

FROM docker-registry.default.svc:5000/phd-assess/node-base:latest

COPY --from=0 /usr/bundle /usr/bundle/
WORKDIR /usr/bundle

CMD node main.js
