FROM golang:1-alpine AS build-env
LABEL maintainer "youyo <1003ni2@gmail.com>"

ENV DIR /go/src/github.com/youyo/zaia
WORKDIR ${DIR}
ADD . ${DIR}
RUN apk add --update make git gcc musl-dev
RUN make download-libs
RUN go build -v

FROM alpine:latest
LABEL maintainer "youyo <1003ni2@gmail.com>"

ENV DIR /go/src/github.com/youyo/zaia
ENV PORT 10050
WORKDIR /app
COPY --from=build-env ${DIR}/zaia /app/zaia
RUN apk add --update --no-cache ca-certificates
EXPOSE ${PORT}/TCP
ENTRYPOINT ["/app/zaia"]
