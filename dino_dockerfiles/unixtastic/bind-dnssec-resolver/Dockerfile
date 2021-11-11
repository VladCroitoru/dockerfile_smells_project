## Standard phusion part
FROM phusion/baseimage:latest
ENV HOME /root
#RUN /etc/my_init.d/00_regen_ssh_host_keys.sh -f                         # Uncomment to Enable SSHD
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh    # Uncomment to Disable SSHD
CMD ["/sbin/my_init"]

## Expose ports.
EXPOSE 53 53/udp

## Application specific part
MAINTAINER Stephen Day <sd@unixtastic.com>
## Setup script - Use a script to reduce the number of created layers.
ADD setup.sh /tmp/setup.sh
RUN /bin/sh /tmp/setup.sh

