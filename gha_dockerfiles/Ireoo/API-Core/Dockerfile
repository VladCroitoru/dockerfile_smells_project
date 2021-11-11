FROM alpine as admin

RUN apk add --no-cache make git
RUN git clone https://github.com/Ireoo/API.admin.git /app
WORKDIR /app
# RUN yarn
# RUN yarn build
# RUN ls -alF
RUN mv ./dist /dist

FROM golang:alpine as builder

RUN apk add --no-cache make git
WORKDIR /api-core-src
COPY --from=tonistiigi/xx:golang / /
COPY . /api-core-src
RUN go mod download
RUN make docker
RUN mv ./bin/API-Core-docker /API-Core
RUN /API-Core
RUN mv ./api-core.conf /api-core.conf

FROM alpine:latest
LABEL org.opencontainers.image.source="https://github.com/Ireoo/API-Core"

RUN apk add --no-cache ca-certificates
COPY --from=builder /API-Core /
COPY --from=builder /api-core.conf /
COPY --from=admin /dist /static
ENTRYPOINT ["/API-Core"]
