# Start from a Debian image with the latest version of Go installed
# and a workspace (GOPATH) configured at /go.
FROM golang

# Copy the local package files to the container's workspace.
ADD . /go/src/surveillance_notify
#RUN apt-get update && apt-get install pkgconf librrd-dev -y
# Build the outyet command inside the container.
# (You may fetch or manage dependencies here,
# either manually or with a tool like "godep".)
RUN go get -v github.com/eclipse/paho.mqtt.golang github.com/op/go-logging github.com/gregdel/pushover
RUN go install surveillance_notify
ENV PREFIX /surveillance
ENV MQTT_HOSTNAME localhost
ENV MQTT_PORT 1883
ENV PUID root
ENV USERTOKEN ""
ENV APPTOKEN ""

USER $PUID

# Run the outyet command by default when the container starts.
WORKDIR /surveillance
ENTRYPOINT /go/bin/surveillance_notify -h $MQTT_HOSTNAME -p $MQTT_PORT -v --usertoken $USERTOKEN --apptoken $APPTOKEN
