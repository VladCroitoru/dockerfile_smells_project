# Use phusion/baseimage as base image. To make your builds
# reproducible, make sure you lock down to a specific version, not
# to `latest`! See
# https://github.com/phusion/baseimage-docker/blob/master/Changelog.md
# for a list of version numbers.
#FROM phusion/baseimage
FROM phusion/passenger-nodejs

# Set correct environment variables.
ENV HOME /root
ENV PUB_FILES /polymer-paper-elements-demo

# Regenerate SSH host keys. baseimage-docker does not contain any, so you
# have to do that yourself. You may also comment out this instruction; the
# init system will auto-generate one during boot.
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# ...put your own build instructions here...

RUN apt-get update --assume-yes --quiet

# Install Stuff
#RUN		apt-get -y install nodejs

# Move into place the App Code
RUN mkdir /polymer-paper-elements-demo
RUN chmod ugoa+rw /polymer-paper-elements-demo
ADD *.jpg /polymer-paper-elements-demo/
ADD *.json /polymer-paper-elements-demo/
ADD *.html /polymer-paper-elements-demo/
ADD *.js /polymer-paper-elements-demo/
RUN chmod ugoa+rw -R /polymer-paper-elements-demo

# Install Bower, install Bower & node dependencies
RUN npm install -g bower
RUN cd /polymer-paper-elements-demo && bower --allow-root install
RUN cd /polymer-paper-elements-demo && npm install
RUN chmod ugoa+rw -R /polymer-paper-elements-demo

# Setup NodeJS Runit script
RUN mkdir /etc/service/nodejs
ADD nodejs_runit.sh /etc/service/nodejs/run
RUN chmod ugoa+x /etc/service/nodejs/run

EXPOSE  80

# Clean up APT when done.
RUN apt-get clean && rm -rf \
	/var/lib/apt/lists/* \
	/tmp/* \
	/var/tmp/* \
	/docker-build
