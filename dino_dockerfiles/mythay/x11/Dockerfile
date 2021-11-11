FROM ubuntu:14.04
MAINTAINER Minglei Hei <mythay@126.com>

# first create user and group for all the X Window stuff
# required to do this first so we have consistent uid/gid between server and client container
RUN addgroup --system xusers \
  && adduser \
			--home /home/xclient \
			--disabled-password \
			--shell /bin/bash \
			--gecos "user for running an xclient application" \
			--ingroup xusers \
			--quiet \
			xclient

# Change to use China mirror, to speed up the apt download speed for test
# RUN sed -i 's/archive.ubuntu/cn.archive.ubuntu/g' /etc/apt/sources.list 

# Install packages required for connecting against X Server
RUN apt-get update && apt-get install -y --no-install-recommends \
				xvfb \
				rxvt \
				xauth \
				x11vnc \
				x11-utils \
				x11-xserver-utils 

# create or use the volume depending on how container is run
# ensure that server and client can access the cookie
RUN mkdir -p /Xauthority && chown -R xclient:xusers /Xauthority
VOLUME /Xauthority

# start x11vnc and expose its port
ENV DISPLAY :0.0
EXPOSE 5900
COPY *.sh /scripts/
RUN chmod +x /scripts/*.sh

# During startup we need to prepare connection to X11-Server container
USER xclient
ENTRYPOINT ["/scripts/x11-entrypoint.sh"]
