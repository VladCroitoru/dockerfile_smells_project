FROM node:8-alpine

RUN set -xe && \

  # Install GIT
  apk add --no-cache git curl gnupg && \

  # Install angular-cli
  export USER=root && export HOME=/tmp && npm install -g @angular/cli

RUN set -e && \
  # Install yarn
  echo '\
        . /etc/profile ; \
    ' >> /root/.profile && \
  curl -o- -L https://yarnpkg.com/install.sh | sh -s -- --stable

COPY ./*.sh /
#CMD ["/entrypoint.sh"]
