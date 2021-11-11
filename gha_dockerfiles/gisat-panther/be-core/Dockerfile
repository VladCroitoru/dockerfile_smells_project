FROM ubuntu

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y curl gdal-bin

RUN curl -sL https://deb.nodesource.com/setup_14.x | bash - \
    && apt-get install -y nodejs

WORKDIR /usr/src/app

COPY . .

RUN npm ci --production-only

EXPOSE 9850-9859

CMD [ "node", "./src/server.js" ]