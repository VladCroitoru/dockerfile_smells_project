FROM ubuntu:18.04

COPY sources.list /etc/apt/sources.list
RUN apt-get update -qq && apt-get install -y --no-install-recommends \
        build-essential \
        git \
        curl

RUN curl --silent --location https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get install --yes nodejs npm
RUN npm install -g cnpm --registry=https://registry.npm.taobao.org

COPY package.json /app/
WORKDIR /app/
RUN npm install

COPY app.js utils.js /app/
COPY keys/key.pem keys/cert.pem /app/keys/


EXPOSE 8443

ENTRYPOINT [ "node", "app.js" ]

