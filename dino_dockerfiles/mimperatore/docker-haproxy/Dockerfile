FROM dockerfile/ubuntu
MAINTAINER mimperatore@gmail.com

# Install Haproxy.
RUN \
  export DEBIAN_FRONTEND=noninteractive && \
  echo "#!/bin/sh\nexit 0" > /usr/sbin/policy-rc.d && \
  sed -i 's/^# \(.*-backports\s\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get install -y inotify-tools haproxy=1.5.3-1~ubuntu14.04.1 && \
  sed -i 's/^ENABLED=.*/ENABLED=1/' /etc/default/haproxy && \
  rm -rf /var/lib/apt/lists/*

# Add files.
ADD haproxy.cfg /etc/haproxy/haproxy.cfg
ADD haproxy.cfg.erb /etc/haproxy/haproxy.cfg.erb
ADD start.bash /haproxy-start

RUN rm /var/run/haproxy.pid

# Define mountable directories.
VOLUME ["/etc/haproxy"]

# Define working directory.
WORKDIR /etc/haproxy

# Define default command.
CMD ["bash", "/haproxy-start"]
