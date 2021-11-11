FROM node:slim

LABEL gurumojo.service=express-api

EXPOSE 8000

COPY bin/healthcheck.sh /usr/local/bin/container-healthcheck
HEALTHCHECK --interval=10s --timeout=3s --retries=3 \
	CMD ["container-healthcheck"]

WORKDIR /opt/gurumojo
COPY package.json package-lock.json /opt/gurumojo/
RUN npm install
# rm -rf ./node_modules ...?
COPY . /opt/gurumojo/

USER node
CMD ["node", "server.js"]
