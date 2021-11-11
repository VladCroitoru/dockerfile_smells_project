FROM efrecon/tcl
MAINTAINER Emmanuel Frecon <emmanuel@sics.se>

# Set the env variable DEBIAN_FRONTEND to noninteractive to get
# apt-get working without error output.
ENV DEBIAN_FRONTEND noninteractive

# Update underlying ubuntu image and all necessary packages, including
# docker itself so it is possible to run containers for sources or
# destinations.
RUN apt-get update
RUN apt-get install -y wget

RUN mkdir -p /opt/watchdog/bin
RUN wget -q -O - https://github.com/coreos/fleet/releases/download/v0.9.1/fleet-v0.9.1-linux-amd64.tar.gz|tar zxf - --wildcards -O */fleetctl > /opt/watchdog/bin/fleetctl
RUN chmod a+x /opt/watchdog/bin/fleetctl

COPY watchdog.tcl /opt/watchdog/
COPY lib/ /opt/watchdog/lib/
COPY bin/ /opt/watchdog/bin/



ENTRYPOINT ["tclsh8.6", "/opt/watchdog/watchdog.tcl"]

