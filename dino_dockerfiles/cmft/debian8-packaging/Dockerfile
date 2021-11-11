FROM debian:jessie
# Add repositories
RUN echo "# add src debian" >> /etc/apt/sources.list
RUN echo "deb-src http://httpredir.debian.org/debian jessie main" >> /etc/apt/sources.list
RUN echo "deb http://httpredir.debian.org/debian jessie-backports main" >> /etc/apt/sources.list
RUN echo "# add other src repositories debian" >> /etc/apt/sources.list
#RUN echo "deb http://httpredir.debian.org/debian sid main" >> /etc/apt/sources.list
RUN echo "deb-src http://httpredir.debian.org/debian jessie-backports main" >> /etc/apt/sources.list
RUN echo "deb-src http://httpredir.debian.org/debian testing main" >> /etc/apt/sources.list
RUN echo "deb-src http://httpredir.debian.org/debian sid main" >> /etc/apt/sources.list
RUN echo "deb-src http://httpredir.debian.org/debian experimental main" >> /etc/apt/sources.list
# Install packages
RUN apt-get update
# Packaging tools
RUN apt-get install --fix-missing -y build-essential devscripts quilt pbuilder lintian pkg-config dh-make
# For packaging python modules that use setuptools
RUN apt-get install -y python-stdeb
# General tools
RUN apt-get install -y vim git subversion ipython
# Cowbuilder
RUN apt-get install -y cowbuilder git-buildpackage
# Prepare environment
ENV DIST jessie-backports
# For quilt (patching tool)
ENV QUILT_PATCHES debian/patches
ENV QUILT_REFRESH_ARGS "-p ab --no-timestamps --no-index"
# For gitlab
ENV GIT_SSL_NO_VERIFY 1
#RUN pbuilder create
