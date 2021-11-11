FROM library/debian:wheezy
MAINTAINER Kenneth Peiruza <kenneth@floss.cat>
# Minimal changes to httpd
RUN apt-get update && \
apt-get -y upgrade && \
apt-get install -y funny-manpages man-db manpages && \
apt-get clean && apt-get autoclean && \
rm -rf /var/lib/apt/lists/*
