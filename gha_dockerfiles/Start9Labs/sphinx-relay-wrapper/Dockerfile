FROM arm32v7/node:12-buster-slim AS builder

WORKDIR /relay
RUN mkdir /relay/.lnd
COPY sphinx-relay/ .
# COPY --chown=1000:1000 sphinx-relay/ .

RUN apt-get update

RUN apt install -y make python-minimal
RUN apt install -y g++ gcc libmcrypt-dev
RUN apt install -y sqlite3

RUN npm install bcrypt
RUN npm install sqlite3
RUN npm install
RUN npm run build

RUN cp /relay/config/app.json /relay/dist/config/app.json
RUN cp /relay/config/config.json /relay/dist/config/config.json

# RUN apt-get update
# RUN apt-get install software-properties-common -y
# RUN apt-get install gnupg -y
# RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys CC86BB64
# RUN add-apt-repository ppa:rmescandon/yq
# RUN apt-get update
# RUN apt-get install yq -y

# RUN chown -R 1000:1000 /relay

RUN npm rebuild

FROM arm32v7/node:12-buster-slim

RUN apt-get update
RUN apt-get install wget -y
RUN wget https://github.com/mikefarah/yq/releases/download/v4.6.3/yq_linux_arm.tar.gz -O - |\
  tar xz && mv yq_linux_arm /usr/bin/yq
RUN apt-get install jq -y
# USER 1000

WORKDIR /relay

COPY --from=builder /relay .

EXPOSE 3300

ENV NODE_ENV production
ENV NODE_SCHEME http
ENV PORT 3300

ADD ./docker_entrypoint.sh /usr/local/bin/docker_entrypoint.sh
ENTRYPOINT ["/usr/local/bin/docker_entrypoint.sh"]
# CMD [ "node", "/relay/dist/app.js" ]
# CMD [ "sh", "-c", "sleep 3000"]