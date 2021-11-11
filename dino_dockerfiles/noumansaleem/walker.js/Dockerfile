FROM node:0.12.5-slim

ADD package.json /tmp/package.json
RUN cd /tmp && npm install
RUN mkdir /src && mv /tmp/node_modules /src

WORKDIR /src
ADD . /src
RUN chmod +x run.sh

ENTRYPOINT ["sh", "run.sh"]
