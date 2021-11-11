FROM golang:1.14.2-alpine AS dev

RUN set -x \
      && apk add --update git make bats lighttpd \
      && go get github.com/cespare/reflex

WORKDIR /go/src/app
COPY . .
VOLUME cmd
CMD [ "sh", "-c", "make; reflex -r '\\.(go|bats|sh|json|mime)$' -- make" ]


FROM dev AS build
RUN set -x \
      && make \
      && rm -rf /app \
      && mkdir -p /app \
      && cp -av ./bin/* /app/


FROM scratch AS framework
WORKDIR /app
COPY --from=build /app/* /app/
