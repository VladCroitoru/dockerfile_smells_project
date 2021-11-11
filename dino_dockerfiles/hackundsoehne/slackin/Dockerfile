FROM node:slim

ENV PORT 3000

ADD . /srv/www

WORKDIR /srv/www

RUN npm install --unsafe-perm

RUN mv ./tools/ENV_VARS.js ./tools/ENV_VARS.temp.js
RUN apt-get update
RUN yes | apt-get install gettext

EXPOSE 3000

ENTRYPOINT ["/bin/bash", "-c", "envsubst < ./tools/ENV_VARS.temp.js > ./tools/ENV_VARS.js && npm start"]
