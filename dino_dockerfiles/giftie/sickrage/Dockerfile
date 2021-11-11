FROM phusion/baseimage:0.9.18
MAINTAINER giftie <giftie61@hotmail.com>
ENV DEBIAN_FRONTEND noninteractive

# Set correct environment variables
ENV HOME /root

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

# Fix a Debianism of the nobody's uid being 65534
RUN usermod -u 99 nobody
RUN usermod -g 100 nobody

RUN add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty universe multiverse"
RUN add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty-updates universe multiverse"
RUN apt-get update -q

# Install Dependencies
RUN apt-get install -qy libxslt1-dev libxslt1.1 libxml2-dev libxml2 libssl-dev libffi-dev python
RUN apt-get install -qy python-pip python-dev libssl-dev git python-cheetah ca-certificates wget unrar unzip
RUN apt-get install -qy build-essential
RUN wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -O - | sudo python2
RUN sudo pip install -U cryptography ndg-httpsclient pyopenssl==0.13.1

RUN rm -f /etc/service/sshd/down
# Regenerate SSH host keys. baseimage-docker does not contain any, so you
# have to do that yourself. You may also comment out this instruction; the
# init system will auto-generate one during boot.
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh

# Install SickRage 0.2.1 (2014-10-22)
RUN mkdir /opt/sickrage
RUN git clone https://github.com/SickRage/SickRage.git /opt/sickrage
RUN chown nobody:users /opt/sickrage
RUN sudo pip -r /opt/sickrage/requirements.txt

EXPOSE 8081

# SickRage Configuration
VOLUME /config

# Downloads directory
VOLUME /downloads

# TV directory
VOLUME /tv

# Add edge.sh to execute during container startup
RUN mkdir -p /etc/my_init.d
ADD edge.sh /etc/my_init.d/edge.sh
RUN chmod +x /etc/my_init.d/edge.sh

# Add SickRage to runit
RUN mkdir /etc/service/sickrage
ADD sickrage.sh /etc/service/sickrage/run
RUN chmod +x /etc/service/sickrage/run
