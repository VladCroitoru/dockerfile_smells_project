#
# Haproxy Dockerfile
#
# https://github.com/llamashoes/haproxy-sshd
#

# Pull base image.
FROM dockerfile/ubuntu

# Install Haproxy.
RUN \
  sed -i 's/^# \(.*-backports\s\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get install -y haproxy=1.5.3-1~ubuntu14.04.1 && \
  sed -i 's/^ENABLED=.*/ENABLED=1/' /etc/default/haproxy

# Install sshd and supervisor
RUN apt-get install -y openssh-server supervisor && \
rm -rf /var/lib/apt/lists/*

RUN mkdir -p /var/run/sshd /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Set root password - will want to change this
RUN echo 'root:changeme' | chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Add files.
ADD haproxy.cfg /etc/haproxy/haproxy.cfg
ADD start.bash /haproxy-start

# Define mountable directories.
VOLUME ["/haproxy-override"]
VOLUME ["/var/log"]

# Define working directory.
WORKDIR /etc/haproxy

# Start supervisord
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]

# Expose ports.
EXPOSE 80
EXPOSE 443
EXPOSE 22
