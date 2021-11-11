# Coturn TURN server in Docker
#
# This Dockerfile creates a container which runs a Coturn TURN server suitable
# for use with Spreed WebRTC.
#
# Install Docker and then run `docker build -t docker-webrtc-turnserver .` to
# build the image.
#
# Due to the nature of TURN, the container needs to use the hosts network. To
# configure the details, create the config file `data/config`. See the example
# in `data/config.example` for some ideas.
# ```
#
# Afterwards run the container like this:
#
#   ```
#   docker run --rm --net=host --name my-spreed-turnserver -i -v `pwd`/data:/srv -t spreed-turnserver
#   ```
#
# This runs the container with the settings as defined in the config file which is # made available to the container using the volume (-v) option. This volume is also
# used as storage for persistent data created by the TURN server.

FROM debian:stretch
MAINTAINER Simon Eisenmann <simon@struktur.de>

ENV DEBIAN_FRONTEND noninteractive

# Install coturn.
RUN apt-get update && apt-get -y install coturn supervisor 
RUN mkdir -p /etc/service/coturn
ADD supervisord.conf /etc/service/coturn/
ADD bootstrap.sh /etc/service/coturn
ADD bootstrap-coturn.sh /etc/service/coturn

# Clean up APT when done.
#RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /etc/service/coturn
RUN chmod 777 /etc/service/coturn/bootstrap-coturn.sh

ENTRYPOINT ["/etc/service/coturn/bootstrap.sh"]