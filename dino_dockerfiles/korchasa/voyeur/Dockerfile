FROM golang:1.9.0-alpine3.6 as builder
WORKDIR /go/src/github.com/korchasa/voyeur
COPY . .
RUN apk add --no-cache git
RUN go get -u github.com/golang/dep/cmd/dep
RUN dep ensure
RUN go test
RUN CGO_ENABLED=0 GOOS=linux go build -o ./voyeur

FROM busybox:1.27.2
COPY --from=builder /go/src/github.com/korchasa/voyeur/voyeur /voyeur
COPY --from=builder /go/src/github.com/korchasa/voyeur/static /static
ARG BUILD_DATE
ARG VCS_REF
LABEL org.label-schema.build-date=$BUILD_DATE \
    org.label-schema.name="voyeur" \
    org.label-schema.description="Monitor HTTP requests between docker containers without pain" \
    org.label-schema.vcs-ref=$VCS_REF \
    org.label-schema.vcs-url="http://github.com/korchasa/voyeur" \
    org.label-schema.schema-version="1.0"
RUN chmod a+x /voyeur
EXPOSE 80
CMD ["/voyeur", "-l", ":80"]