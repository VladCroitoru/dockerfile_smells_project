FROM node:8.7.0-alpine

ARG BUILD_DATE
ARG VCS_REF

ENV POLYMER_CLI_VERSION=1.5.6
ENV BOWER_VERSION=1.8.0

RUN apk add -U --virtual .tools git sudo bash openssh-client && \
    npm i polymer-cli@${POLYMER_CLI_VERSION} bower@${BOWER_VERSION} -g --unsafe-perm  && \
    echo 'export PS1="\W > "' > /home/node/.bashrc && \
    echo "prefix=/home/node/.npm-packages" > ~/.npmrc

ENV PATH /home/node/.npm-packages/bin:$PATH

COPY entrypoint.sh /usr/local/bin
COPY filterDoc.js /usr/local/bin/filterDoc

LABEL MAINTAINER="F. Le Coz <fabrice.lecoz@zedesk.net>" \
      POLYMER_CLI_VERSION=${POLYMER_CLI_VERSION} \
      NODE_VERSION="8.7.0" \
      NPM_VERSION="5.4.2" \
      BOWER_VERSION=${BOWER_VERSION} \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/zedesk/zdkpolymer.git" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.schema-version="1.0.0-rc1"

# Drop privileges
USER node

VOLUME ["/app","/home/node"]
WORKDIR "/app"
EXPOSE 8081 8080
ENTRYPOINT ["entrypoint.sh"]
