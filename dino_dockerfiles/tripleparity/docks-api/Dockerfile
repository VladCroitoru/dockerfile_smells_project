# --------------------------------------------
# Use this stage to build all the node modules
# --------------------------------------------

FROM node:9.8.0-alpine AS node-dependencies

RUN apk add --update python make g++ openssl

WORKDIR /app
COPY package*.json ./
RUN npm install --only=production

WORKDIR /tmp
RUN wget https://download.docker.com/linux/static/stable/x86_64/docker-18.06.0-ce.tgz && \
    tar xvf docker-18.06.0-ce.tgz

# ----------------------
# Actual image
# ----------------------

FROM node:9.8.0-alpine

RUN apk add --update postgresql-client

EXPOSE 8080

WORKDIR /app

COPY --from=node-dependencies /app/node_modules /app/node_modules
COPY --from=node-dependencies /tmp/docker/docker /usr/bin/docker
COPY . .

CMD ["/app/scripts/docks-prod-start.sh"]
