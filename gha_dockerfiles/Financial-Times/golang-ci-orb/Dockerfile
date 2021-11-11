FROM golang:1

ENV PROJECT=orb-integration-tests

COPY . "/${PROJECT}"
WORKDIR "/${PROJECT}"

RUN go build -mod=readonly -a -o /artifacts/${PROJECT}

# Multi-stage build - copy certs and the binary into the image
FROM scratch
WORKDIR /
COPY --from=0 /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=0 /artifacts/* /
CMD [ "/orb-integration-tests" ]
