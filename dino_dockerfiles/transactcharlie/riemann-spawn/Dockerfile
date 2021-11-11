# Intermediary Build Container
FROM golang:1.9

RUN mkdir -p /go/src/github.com/transactcharlie/riemann-spawn
WORKDIR /go/src/github.com/transactcharlie/riemann-spawn
COPY . .
RUN go get
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o riemann-spawn .



# Final (static from scratch container)
FROM scratch

ARG VCS_REF
ARG BUILD_DATE

MAINTAINER TransactCharlie
LABEL org.label-schema.name="riemann-spawn" \
      org.label-schema.description="Sends repeated events to riemann for testing" \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/TransactCharlie/riemann-spawn"

COPY --from=0 /go/src/github.com/transactcharlie/riemann-spawn/riemann-spawn /riemann-spawn
CMD ["/riemann-spawn"]
