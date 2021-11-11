FROM phusion/baseimage:0.9.15
MAINTAINER Navvy "navvy144@gmail.com"
ENV REFRESHED_AT 2016-01-04
ENV DEBIAN_FRONTEND noninteractive
ENV HOME /root

# Add config.sh to execute during container startup
ADD config.sh /etc/my_init.d/config.sh
RUN chmod +x /etc/my_init.d/*

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

# chfn workaround - Known issue within Dockers
RUN ln -s -f /bin/true /usr/bin/chfn

#install dependancies
RUN apt-get update && apt-get install -y wget

#map array
VOLUME /mnt

#get retrospect
RUN wget https://s3.amazonaws.com/download.retrospect.com/software/linux/v1100/Linux_Client_x64_11_0_0_107.tar \
 && tar xvf Linux_Client_x64_11_0_0_107.tar

#get modified install script
ADD Retroinstall.sh /tmp/Retroinstall.sh
RUN chmod 755 /tmp/Retroinstall.sh

#install retrospect
RUN /tmp/Retroinstall.sh

#Add default retro password
ADD retroclient.state /var/log/retroclient.state

#start retrospect
ENTRYPOINT /usr/local/retrospect/client/retroclient

#open ports
EXPOSE 497

