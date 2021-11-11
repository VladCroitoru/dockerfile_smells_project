FROM node:8.11.4-alpine AS registry_builder
RUN mkdir /app-build
RUN apk update && apk add python make g++ curl bash
WORKDIR /app-build
COPY . /app-build
RUN chown -R node:node /app-build /usr/local/lib/node_modules
RUN curl https://install.meteor.com/ | sh
RUN npm install -g maka-cli --unsafe
USER node
RUN maka npm install && maka build
#RUN maka npm install --save babel-runtime


FROM debian:jessie
MAINTAINER Luke Campbell <luke.campbell@rpsgroup.com>

ENV REGISTRY_VERSION 1.2.1

ENV NODE_VERSION 4.6.1
ENV GOSU_VERSION 1.9
ENV SCRIPTS_DIR /opt/build_scripts
ENV BUILD_DIR /opt/build_dir
ENV APP_DIR /opt/meteor/dist
ENV PORT 3000

RUN mkdir -p $SCRIPTS_DIR
RUN useradd -m node

COPY --from=registry_builder /app-build/build $BUILD_DIR/
COPY contrib/scripts/ $SCRIPTS_DIR/

RUN $SCRIPTS_DIR/install-deps.sh
RUN $SCRIPTS_DIR/install-node.sh

RUN $SCRIPTS_DIR/install-app.sh
WORKDIR $APP_DIR/bundle

CMD ["/usr/local/bin/gosu", "node", "node", "main.js"]
