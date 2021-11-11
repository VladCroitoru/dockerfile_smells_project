FROM node:8.9.4-alpine

WORKDIR /usr/src

ENV ANGULAR_CLI_VERSION v1.7.0
ENV STYLELINT_VERSION 9.1.1
RUN yarn global add @angular/cli@${ANGULAR_CLI_VERSION} \
    && ng new angular \
    && cd angular \
    && yarn add stylelint@${STYLELINT_VERSION} \
                stylelint-scss \
                stylelint-config-sass-guidelines \
                stylelint-order \
                stylelint-scss

ENV PATH ${PATH}:/usr/src/angular/node_modules/.bin
WORKDIR /usr/src/angular
COPY src /usr/src/angular/src/
CMD ["exec", "$@"]
