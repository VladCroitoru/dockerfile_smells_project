# Server Builder
FROM golang:1.8-alpine as server-builder
WORKDIR /go/src/github.com/hyperscale/hyperpaas/
RUN apk add --update --no-cache ca-certificates curl git make && rm -rf /var/cache/apk/*
RUN curl https://glide.sh/get | sh
COPY ./ .
RUN make deps
RUN make build
RUN chmod +x hyperpaas

# UI Builder
FROM node:6.11-alpine as ui-builder
WORKDIR /build/
COPY ./ui/ .
RUN npm install -g @angular/cli
RUN npm install
RUN ng build --target=production --environment=prod --sourcemap --aot --base-href=/ui/

# Application
FROM docker:17.07.0-ce-dind
LABEL maintainer "Axel Etcheverry <axel@etcheverry.biz>"
ENV PORT 8080
ENV DEBUG true
RUN apk add --update --no-cache ca-certificates curl && rm -rf /var/cache/apk/*
WORKDIR /opt/hyperpaas/
COPY --from=server-builder /go/src/github.com/hyperscale/hyperpaas/hyperpaas .
COPY --from=ui-builder /build/dist ./ui/
HEALTHCHECK --interval=5s --timeout=2s CMD curl -f http://localhost:${PORT}/health > /dev/null 2>&1 || exit 1
EXPOSE ${PORT}
VOLUME /var/lib/hyperpaas
ENTRYPOINT ["/usr/local/bin/dockerd-entrypoint.sh", "/opt/hyperpaas/hyperpaas"]
