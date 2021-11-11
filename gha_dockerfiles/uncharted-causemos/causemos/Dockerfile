# docker build -t docker.uncharted.software/worldmodeler/wm-server:latest .

FROM mhart/alpine-node:12
# ENV LOG_LEVEL="warn"

RUN apk update && apk add curl

ADD ./package.json /package.json
ADD ./yarn.lock /yarn.lock
ADD ./server/src /server/src
ADD ./server/public /server/public
ADD ./server/docker_scripts /server/docker_scripts
ADD ./server/package.json /server/package.json
# ADD ./server/package-lock.json /wm-server/package-lock.json


# When running as root, npm won't run any scripts by default. --unsafe-perm let npm to run the scripts
#
# `If npm was invoked with root privileges, then it will change the uid to the user account or uid specified by the user config, which defaults to nobody. Set the unsafe-perm flag to run scripts with root privileges.`
# Ref: https://docs.npmjs.com/misc/scripts#user

# Hack: get around docker-compose needing wm-server - Feb 11, 2021
RUN ln -s /server /wm-server

WORKDIR /server

# HEALTHCHECK --interval=20s --timeout=2s --start-period=60s \
# CMD node ./docker_scripts/health_check.js

WORKDIR /
RUN yarn install
CMD yarn workspace server run start --log-level info

