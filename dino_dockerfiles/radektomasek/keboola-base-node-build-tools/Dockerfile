# VERSION 1.1.0
FROM radektomasek/keboola-base-node
MAINTAINER Radek Tomasek <radek.tomasek@gmail.com>

WORKDIR /tmp

# Install dev-tools dependencies required by some npm modules (make, gcc).
RUN yum install -y make tar gcc gcc-c++ ncurses-devel readline-devel gnutls-devel || true
