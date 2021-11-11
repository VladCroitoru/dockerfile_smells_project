# Use phusion/baseimage as base image. To make your builds reproducible, make
# sure you lock down to a specific version, not to `latest`!
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for
# a list of version numbers.
FROM phusion/baseimage:0.9.18
MAINTAINER Warehouseman "mhb.warehouseman@gmail.com"

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US
RUN locale-gen en_US.UTF-8

RUN add-apt-repository ppa:x2go/stable

RUN DEBIAN_FRONTEND=noninteractive apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get upgrade -y -o Dpkg::Options::="--force-confold" \
 && DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade -y -o Dpkg::Options::="--force-confold"
 
RUN DEBIAN_FRONTEND=noninteractive apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y xubuntu-desktop
    
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y \
    x2goserver \
    x2goserver-xsession \
    nano \
    lshw \
    gettext \
    gedit \
    gnome-terminal \
 && apt-get clean \
 && apt-get -y autoremove

RUN echo -e "\n\n\n* * *  Preparing SSH Host Keys  * * * \n\n"
RUN rm -f /etc/service/sshd/down
# Regenerate SSH host keys. baseimage-docker does not contain any, so you
# have to do that yourself. You may also comment out this instruction; the
# init system will auto-generate one during boot.
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh

RUN echo -e "\n\n\n* * *  Cleaning up  * * * \n\n"
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install init script to add SSH keys
ADD add_ssh_env_keys.sh /etc/my_init.d/
RUN chmod +x /etc/my_init.d/*.sh

RUN DEBIAN_FRONTEND=noninteractive apt-get clean && apt-get -y autoremove



