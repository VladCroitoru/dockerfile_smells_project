FROM ubuntu:xenial
MAINTAINER Jan Blaha

RUN apt-get update && apt-get install -y curl sudo && \
    curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash - && \
    apt-get install -y nodejs default-jre unzip && \
    curl -o fop.zip apache.miloslavbrada.cz/xmlgraphics/fop/binaries/fop-2.1-bin.zip && \
    unzip fop.zip && \
    rm fop.zip && \
    chmod +x fop-2.1/fop

ENV PATH "$PATH:/fop-2.1"

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.json /usr/src/app/
RUN npm install --production

COPY . /usr/src/app

EXPOSE 6000

HEALTHCHECK CMD curl --fail http://localhost:6000 || exit 1

CMD [ "node", "index.js" ]