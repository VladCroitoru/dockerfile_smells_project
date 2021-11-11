# Ubuntu HAProxy.

FROM ubuntu:14.04
MAINTAINER Thomas Quintana <thomas@bettervoice.com>

# Add the latest stable haproxy ppa.
RUN apt-get update && apt-get install -y software-properties-common
RUN add-apt-repository ppa:vbernat/haproxy-1.5

# Install.
RUN apt-get update && apt-get install -y haproxy

# Enable logging.
ADD conf/rsyslog.conf /etc/rsyslog.conf
ADD conf/50-default.conf /etc/rsyslog.d/50-default.conf

# Start HAProxy.
CMD service rsyslog restart && service haproxy start && tail -f /var/log/syslog