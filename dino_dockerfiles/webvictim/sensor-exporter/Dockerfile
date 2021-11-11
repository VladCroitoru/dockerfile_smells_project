# Start from a Debian image with the latest version of Go installed
# and a workspace (GOPATH) configured at /go.
FROM golang:latest

# Copy the local package files to the container's workspace.
ADD sensor-exporter /go/src/github.com/ncabatoff/sensor-exporter

# Build the outyet command inside the container.
# (You may fetch or manage dependencies here,
# either manually or with a tool like "godep".)
RUN apt-get update && apt-get --yes install libsensors4-dev && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN go get github.com/md14454/gosensors github.com/prometheus/client_golang/prometheus && go install github.com/ncabatoff/sensor-exporter

# Run the output command by default when the container starts.
ENV HDDTEMP_HOSTNAME=172.17.0.1
ENTRYPOINT /go/bin/sensor-exporter -hddtemp-address $HDDTEMP_HOSTNAME:7634

# Document that the service listens on port 9255.
EXPOSE 9255
