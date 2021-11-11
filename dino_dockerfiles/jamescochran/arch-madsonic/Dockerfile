FROM binhex/arch-base:latest
MAINTAINER binhex

# additional files
##################

# add supervisor conf file for app
ADD setup/*.conf /etc/supervisor/conf.d/

# add bash scripts to install app
ADD setup/root/*.sh /root/

# copy start bash script to madsonic dir (checks ssl enabled/disabled and copies transcoders to madsonic install dir)
ADD setup/nobody/*.sh /home/nobody/

# install app
#############

# make executable and run bash scripts to install app
RUN chmod +x /root/*.sh /home/nobody/*.sh && \
	/bin/bash /root/install.sh

# docker settings
#################

# set env variable for java
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk/jre

# map /config to host defined config path (used to store configuration from app)
VOLUME /config

# map /media to host defined media path (used to read/write to media library)
VOLUME /media

# expose port for http
EXPOSE 4040

# expose port for https
EXPOSE 4050

# set permissions
#################

# run script to set uid, gid and permissions
CMD ["/bin/bash", "/root/init.sh"]