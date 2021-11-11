FROM phusion/baseimage:0.9.11
MAINTAINER deemos <robberhines@gmail.com>
ENV DEBIAN_FRONTEND noninteractive

# Set correct environment variables
ENV HOME /root
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
RUN locale-gen en_US en_US.UTF-8
RUN update-locale LANG=en_US.UTF-8
RUN dpkg-reconfigure locales

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

# Fix a Debianism of the nobody's uid being 65534
RUN usermod -u 99 nobody
RUN usermod -g 100 nobody
RUN apt-get update -qq

# Install McMyAdmin run dependencies
RUN apt-get install -qy --force-yes libmono-cil-dev Libgdiplus unzip wget

WORKDIR /usr/local
RUN wget http://mcmyadmin.com/Downloads/etc.zip && unzip etc.zip && rm etc.zip

# Install McMyAdmin
RUN mkdir mkdir /opt/McMyAdmin && \
    cd /opt/McMyAdmin && \
    wget -nv -O MCMA2_glibc26_2.zip http://mcmyadmin.com/Downloads/MCMA2_glibc26_2.zip?dl=1 && \
    unzip MCMA2_glibc26_2.zip && \
    rm MCMA2_glibc26_2.zip

RUN cd /opt/McMyAdmin; /opt/McMyAdmin/MCMA2_Linux_x86_64 -configonly -nonotice -nostart -updateonly > /dev/null 2>&1	
	
# Open ports
EXPOSE      8080
EXPOSE      25565

#VOLUMES
VOLUME /config
RUN rm -rf /opt/McMyAdmin/ProgramData-Server && \
    ln -sf /config/ /opt/McMyAdmin/ProgramData-Server && \
    chown -R nobody:users /opt/McMyAdmin
