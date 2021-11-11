FROM phusion/baseimage:0.9.16
ENV DEBIAN_FRONTEND noninteractive
# Set correct environment variables
ENV HOME /root
# Set the locale
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8 

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]
# Fix a Debianism of the nobody's uid being 65534
RUN usermod -u 99 nobody && \
usermod -g 100 nobody && \
add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty universe multiverse" && \
add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty-updates universe multiverse" && \
apt-get update -q && \
# Install Dependencies
apt-get install -qy python python-cheetah ca-certificates wget unzip unrar && \
# Get  Moviegrabber
cd /root && \
wget https://github.com/binhex/moviegrabber/archive/stable.zip && \
unzip stable.zip && \
mv moviegrabber-stable /opt/moviegrabber && \
chown -R nobody:users /opt/moviegrabber
EXPOSE 9191
# Moviegrabber Configuration
VOLUME /config

# Watch-Folder/Movies
VOLUME /watchfolder
VOLUME /movies


# Add Moviegrabber to runit
RUN mkdir /etc/service/moviegrabber
ADD moviegrabber.sh /etc/service/moviegrabber/run
RUN chmod +x /etc/service/moviegrabber/run
