# HEADER
FROM        alpine:latest
MAINTAINER  rkosyk

# Install Quagga
RUN         apk --no-cache add quagga supervisor

# Supervisord
ADD         supervisord.conf /etc/supervisord.conf

# Configuration files
# VOLUME /etc/quagga

# Expose ports
# EXPOSE 2601 2604

# Command
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
