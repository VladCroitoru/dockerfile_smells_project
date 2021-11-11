FROM node:7-onbuild

RUN mv ./tools/ENV_VARS.js ./tools/ENV_VARS.temp.js
RUN apt-get update
RUN yes | apt-get install gettext

EXPOSE 8080

ENTRYPOINT ["/bin/bash", "-c", "envsubst < ./tools/ENV_VARS.temp.js > ./tools/ENV_VARS.js && npm start"]
