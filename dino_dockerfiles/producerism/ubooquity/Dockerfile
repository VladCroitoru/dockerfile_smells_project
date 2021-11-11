#Ubooquity
FROM ubuntu:trusty
MAINTAINER Carlos Hernandez <carlos@techbyte.ca>

# Let the container know that there is no tty
ENV DEBIAN_FRONTEND noninteractive

# Set locale to UTF-8
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
RUN locale-gen en_US en_US.UTF-8
RUN update-locale LANG=en_US.UTF-8
RUN dpkg-reconfigure locales

# Set user nobody to uid and gid of unRAID, uncomment for unRAID
RUN usermod -u 99 nobody
RUN usermod -g 100 nobody
RUN usermod -s /bin/bash nobody

# Update ubuntu
RUN apt-mark hold initscripts udev plymouth mountall;\
    echo 'APT::Get::Assume-Yes "true";' > /etc/apt/apt.conf.d/90forceyes;\
    echo 'deb http://archive.ubuntu.com/ubuntu trusty main universe restricted' > /etc/apt/sources.list;\
    echo 'deb http://archive.ubuntu.com/ubuntu trusty-updates  main universe restricted' >> /etc/apt/sources.list;\
    apt-get update;\
    echo exit 101 > /usr/sbin/policy-rc.d && chmod +x /usr/sbin/policy-rc.d;\
    dpkg-divert --local --rename --add /sbin/initctl;\
    ln -sf /bin/true /sbin/initctl;\
    apt-get -y upgrade && apt-get clean

# Install dependencies
RUN apt-get install -qy --force-yes openjdk-7-jre-headless wget python-pip unzip python-tornado python-zmq python-psutil \
    && apt-get clean

# Install and Configure Circus
RUN pip --no-input install --upgrade pip
RUN pip --no-input install circus;\
    pip --no-input install envtpl
RUN mkdir /etc/circus.d /etc/setup.d

# Install Ubooquity
#RUN wget http://vaemendis.net/ubooquity/downloads/Ubooquity-1.8.2.zip && unzip Ubooquity-1.8.2.zip -d UbooquityInstall
RUN wget -O ubooquity.zip http://vaemendis.net/ubooquity/service/download.php && unzip ubooquity.zip -d UbooquityInstall

# Exposed config volume
VOLUME /config

# Add config files
ADD ./files/circus.ini /etc/circus.ini
ADD ./files/start.sh /start.sh
ADD ./files/setup.d/Ubooquity /etc/setup.d/Ubooquity
ADD ./files/circus.d/Ubooquity.ini.tpl /etc/circus.d/Ubooquity.ini.tpl

# change ownership for unRAID
RUN chown -R nobody:users /UbooquityInstall

# Expose default Ubooquity port
EXPOSE 8085
# Make start script executable and default command
RUN chmod +x /start.sh
ENTRYPOINT ["/start.sh"]
