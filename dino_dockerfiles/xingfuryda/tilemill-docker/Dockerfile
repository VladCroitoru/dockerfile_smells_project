## -*- docker-image-name: "xingfuryda/tilemill-docker:latest" -*-

##
# The Tilemill Docker Server
#
# This creates an image with tilemill hosted as a nodejs
# web app for remote use

FROM phusion/baseimage:0.9.17
MAINTAINER xingfuryda

# install packages
RUN apt-get update -yq
RUN apt-get install -yq nodejs-legacy npm build-essential g++ git libgtk2.0-dev ttf-dejavu fonts-droid ttf-unifont fonts-sipa-arundina fonts-sil-padauk fonts-khmeros ttf-indic-fonts-core fonts-taml-tscu ttf-kannada-fonts

# build tilemill
RUN mkdir /home/root
RUN cd /home/root && git clone https://github.com/mapbox/tilemill.git && cd tilemill && git checkout 8044976d3d0a1b78de663c24009239994db76b7b .
RUN cd /home/root/tilemill && npm install

# force qs version 5.2.0
RUN cd /home/root/tilemill/node_modules/connect && rm -rf node_modules
RUN sed -i 's/>= 0.4.0/5.2.0/' /home/root/tilemill/node_modules/connect/package.json
RUN cd /home/root/tilemill/node_modules/connect && npm install

# Create a `tilemill` `runit` service
ADD tilemill /etc/sv/tilemill
RUN chmod +x /etc/sv/tilemill/run
RUN update-service --add /etc/sv/tilemill

# Add environment variables for server addresses
ENV COREURL core.tmserver.org
ENV TILEURL tile.tmserver.org

# Clean up APT when done
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Expose the webserver ports
EXPOSE 20008
EXPOSE 20009

# Add the README
ADD README.md /usr/local/share/doc/

# Add the help file
RUN mkdir -p /usr/local/share/doc/run
ADD help.txt /usr/local/share/doc/run/help.txt

# Add the entrypoint
ADD run.sh /usr/local/sbin/run
RUN chmod +x /usr/local/sbin/run
ENTRYPOINT ["/sbin/my_init", "--", "/usr/local/sbin/run"]