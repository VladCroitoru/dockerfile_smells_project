FROM alpine

RUN apk update \
  && apk upgrade \
  && apk add --update tini \
  && apk add --no-cache build-base cmake git ruby ruby-dev ruby-json ruby-io-console nodejs yarn

RUN gem install --no-document pronto \
  && gem install --no-document pronto-eslint_npm

CMD ["pronto", "run"]
