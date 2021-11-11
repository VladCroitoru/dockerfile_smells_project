FROM efrecon/mini-tcl:3.7
MAINTAINER Emmanuel Frecon <emmanuel@sics.se>

# Install git so we can install dependencies and install socat so we
# can talk to the docker daemon.
RUN mkdir -p /opt/docker2stomp/lib && \
    apk add --no-cache git socat && \
    git clone https://github.com/efrecon/tcl-stomp /tmp/tcl-stomp && \
    rm -rf /tmp/tcl-stomp/.git && \
    mv /tmp/tcl-stomp/lib/stomp /opt/docker2stomp/lib/ && \
    apk del git

# COPY code
COPY stomper.tcl /opt/docker2stomp/
COPY lib/tockler/*.tcl /opt/docker2stomp/lib/tockler/

VOLUME ["/tmp/docker.sock"]

ENTRYPOINT ["tclsh8.6", "/opt/docker2stomp/stomper.tcl", "-docker", "unix:///tmp/docker.sock", "-verbose", "3"]
