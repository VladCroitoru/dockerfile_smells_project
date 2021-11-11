# builder image
FROM golang:1.11 as builder

RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get update -y && apt-get upgrade -y && \
    apt-get -y install git && apt-get -y autoclean

COPY src/github.com/webofmars/oncall-buddy-finder/ /go/src/oncall-buddy-finder
WORKDIR /go/src/oncall-buddy-finder

RUN go get -v -d .
RUN CGO_ENABLED=0 GOOS=linux go build \
        -i -v -a -installsuffix cgo -gcflags "all=-N -l" \
        -o oncall-buddy-finder .

# adds delve
RUN go get github.com/derekparker/delve/cmd/dlv && \
    cd /go/src/github.com/derekparker/delve/cmd/dlv && \
    CGO_ENABLED=0 GOOS=linux go build \
        -i -v -a -installsuffix cgo -gcflags "all=-N -l" \
        -o /go/src/oncall-buddy-finder/dlv

# The final image
FROM alpine:3.8

LABEL maintainer="contact@webofmars.com"

# libc6-compat is used when debugging with delve
RUN apk add --no-cache libc6-compat tzdata ca-certificates curl && \
    mkdir /var/run/oncall-buddy-finder && \
    chmod 777 /var/run/oncall-buddy-finder

COPY etc/ /etc/oncall-buddy-finder/
COPY --from=builder /go/src/oncall-buddy-finder/dlv /usr/local/bin/
COPY --from=builder /go/src/oncall-buddy-finder/oncall-buddy-finder /usr/local/bin/

VOLUME /etc/oncall-buddy-finder
VOLUME /var/run/oncall-buddy-finder
WORKDIR /usr/local/bin
EXPOSE 8000
ENV CONFIG=/etc/oncall-buddy-finder/config-docker.json
USER nobody
HEALTHCHECK --interval=10s --retries=3 --start-period=10s --timeout=1s \
    CMD [ "curl", "-f", "http://localhost:8000/buddy" ]
ENTRYPOINT ["/usr/local/bin/oncall-buddy-finder"]