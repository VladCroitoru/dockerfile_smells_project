FROM  node:11-alpine

ARG NG_CLI_VERSION

ENV NG_CLI_VERSION ${NG_CLI_VERSION:-7.3.8}

RUN \
  echo "$NG_CLI_VERSION" && \
  npm install -g @angular/cli@${NG_CLI_VERSION} && \
  ng version
