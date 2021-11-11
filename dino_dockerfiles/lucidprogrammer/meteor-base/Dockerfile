FROM buildpack-deps:jessie
LABEL Lucid Programmer <lucidprogrammer@hotmail.com>
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y locales && \
	echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen en_US.UTF-8 && \
    dpkg-reconfigure locales && \
    /usr/sbin/update-locale LANG=en_US.UTF-8 && \
		apt-get install -y \
					  xvfb \
					  x11-xkb-utils \
					  xfonts-100dpi \
					  xfonts-75dpi \
					  xfonts-scalable \
					  xfonts-cyrillic \
					  x11-apps \
					  clang \
					  libdbus-1-dev \
					  libgtk2.0-dev \
					  libnotify-dev \
					  libgnome-keyring-dev \
					  libgconf2-dev \
					  libasound2-dev \
					  libcap-dev \
					  libcups2-dev \
					  libxtst-dev \
					  libxss1 \
					  libnss3-dev \
					  gcc-multilib \
					  g++-multilib
ARG METEOR_VERSION
ENV METEOR_VERSION ${METEOR_VERSION}

RUN curl "https://install.meteor.com/?release=${METEOR_VERSION}" | /bin/sh
ENV dev_bundle=${METEOR_VERSION}

ENV PATH=$PATH:/root/.meteor/packages/meteor-tool/$dev_bundle/mt-os.linux.x86_64/dev_bundle/bin:/root/.meteor/packages/meteor-tool/$dev_bundle/mt-os.linux.x86_64/dev_bundle/mongodb/bin \
    NODE_PATH=/root/.meteor/packages/meteor-tool/$dev_bundle/mt-os.linux.x86_64/dev_bundle/lib/node_modules:/root/.meteor/packages/meteor-tool/$dev_bundle/mt-os.linux.x86_64/dev_bundle/server-lib/node_modules\
    METEOR_ALLOW_SUPERUSER=true\
		TOOL_NODE_FLAGS="--max-old-space-size=2048"\
		LC_ALL=en_US.UTF-8\
		PORT=80
RUN mkdir -p /data/meteor_uploads
