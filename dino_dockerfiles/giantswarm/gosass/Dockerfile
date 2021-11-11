FROM jbergknoff/sass

RUN ln -s /usr/bin/sass /usr/bin/sassc
RUN apk update && apk add curl \
  && curl -SL https://github.com/giantswarm/gosass/releases/download/v0.1.0/gosass \
    -o /usr/bin/gosass \
  && chmod u+x /usr/bin/gosass \
  && apk del curl

ENTRYPOINT ["gosass"]
